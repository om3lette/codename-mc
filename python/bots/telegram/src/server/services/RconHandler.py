import logging

import aiomcrcon
from python.bots.common import RconConfigSchema
from unidecode import unidecode


class RconHandler:
	def __init__(self, server_address: str, config: RconConfigSchema):
		self.__address: str = server_address
		self.__config: RconConfigSchema = config

	@property
	def is_configured(self):
		return self.__config.password is not None and self.__config.password != ""

	async def execute(self, command: str) -> str | None:
		# Remove "/" from command if present, convert all Unicode characters to ascii (it is required)
		command: str = unidecode(command.replace("/", "", 1))
		try:
			async with aiomcrcon.Client(
				self.__address, self.__config.password, self.__config.port
			) as client:
				return await client.command(command)
		except (OSError, TimeoutError, UnicodeEncodeError) as e:
			if e is OSError:
				logging.critical(
					"Unable to connect to rcon. Check firewall settings and port availability"
				)
			elif e is UnicodeEncodeError:
				logging.critical("Failed to convert string to ascii characters")
			else:
				logging.critical(
					"Unable to connect to rcon. Connection timed out. Check the provided SERVER_ADDRESS for errors"
				)
			return None
