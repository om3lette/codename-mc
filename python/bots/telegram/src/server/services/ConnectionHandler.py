import asyncio
import logging
from datetime import timedelta, datetime

from mcstatus import JavaServer
from typing import Callable, Optional

from mcstatus.status_response import JavaStatusResponse

from python.bots.telegram.src.constants import config
from aiogram.types import Message

from python.bots.telegram.src.server.schemas.RequestCache import RequestCacheSchema
from python.bots.telegram.src.utils import default_ping_error_callback


class ConnectionHandler:
	_cache: dict[str, RequestCacheSchema] = {}
	_cache_expire_time: dict[str, timedelta] = {
		"async_ping": timedelta(seconds=5),
		"get_server_status": timedelta(seconds=5)
		if config.dev_mode
		else timedelta(minutes=1),
		"query_server": timedelta(seconds=5)
		if config.dev_mode
		else timedelta(minutes=1),
	}

	def __init__(self, server_address: str):
		self.server_address: str = server_address
		self.connection: JavaServer = JavaServer.lookup(self.server_address)

	async def __is_connected(
		self, error_callback: Callable = lambda *args: None
	) -> bool:
		attempt_number: int = 1
		while attempt_number <= config.connection.max_retries_before_hangup:
			try:
				await self.connection.async_ping()
				return True
			except ConnectionRefusedError:
				logging.error(f"Ping №{attempt_number} failed")
				# Attempt number, is attempt final
				await error_callback(
					attempt_number,
					attempt_number == config.connection.max_retries_before_hangup,
				)
				if attempt_number != config.connection.max_retries_before_hangup:
					await asyncio.sleep(config.connection.seconds_between_retries)
				attempt_number += 1
		logging.critical("Server is down. Calling admins")
		return False

	async def get_server_status(self) -> JavaStatusResponse:
		return await self.connection.async_status()

	async def query_server(self):
		try:
			return await self.connection.async_query()
		except TimeoutError:
			logging.critical(
				"'query' has to be enabled in a server's server.properties file!"
			)
			return None

	def __get_cache(
		self, function_name: str, user_id
	) -> tuple[Optional[RequestCacheSchema], bool]:
		cache_value: RequestCacheSchema = self._cache.get(function_name)
		expire_time: timedelta | None = self._cache_expire_time.get(function_name)
		if expire_time is None:
			logging.warning(
				f"No cache expire time found for '{function_name}', cache is not used"
			)
			expire_time = timedelta(seconds=0)

		if cache_value is None:
			logging.debug("Cache miss")
			return None, False

		has_expired: bool = cache_value.has_expired(expire_time)
		if not has_expired and (user_id not in config.admins.ids or config.dev_mode):
			logging.debug("Cache hit")
			return cache_value.data, True
		if has_expired:
			logging.debug("Cache expired")
			del self._cache[function_name]
			return None, False
		logging.debug("Cache ignored. User is an admin")
		return None, False

	async def execute(
		self, request_message: Message, func: Callable
	) -> tuple[bool, any]:
		cached_data, is_cache_valid = self.__get_cache(
			func.__name__, request_message.from_user.id
		)
		if is_cache_valid:
			return True, cached_data
		if not await self.__is_connected(
			lambda x, y: default_ping_error_callback(request_message, x, y)
		):
			return False, None
		response: any = await func()
		self._cache[func.__name__] = RequestCacheSchema(
			data=response, timestamp=datetime.now()
		)
		return True, response
