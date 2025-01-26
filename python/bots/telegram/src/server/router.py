from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.enums import ParseMode
from mcstatus.status_response import JavaStatusPlayers

from python.bots.telegram.src.buttons.builders import players_markup_builder
from python.bots.telegram.src.constants import config
from python.bots.telegram.src.handlers import connection_handler, rcon_handler
import python.bots.telegram.src.response_messages as messages

server_router: Router = Router()


@server_router.message(Command("is_alive"))
async def check_server_status(message: Message):
	[is_alive, response_time] = await connection_handler.execute(
		message, connection_handler.connection.async_ping
	)
	if not is_alive:
		return
	await message.reply(messages.PING_SUCCESS.format(latency=round(response_time, 2)))


@server_router.message(Command("current_online"))
async def players_number(message: Message):
	[is_alive, status] = await connection_handler.execute(
		message, connection_handler.get_server_status
	)
	if not is_alive:
		return
	players: JavaStatusPlayers = status.players
	await message.reply(
		messages.PLAYERS_NUMBER.format(
			current_number=players.online, capacity=players.max
		)
	)


@server_router.message(Command("players_online"))
async def players_list(message: Message):
	[is_alive, server_status] = await connection_handler.execute(
		message, connection_handler.get_server_status
	)
	if not is_alive:
		return
	players: JavaStatusPlayers = server_status.players
	if players.sample is None or len(players.sample) == 0:
		await message.reply(messages.PLAYERS_ONLINE + "\n" + messages.NO_PLAYERS_ONLINE)
		return
	usernames: list[str] = [player.name for player in players.sample]
	new_markup, exit_status = players_markup_builder.build(usernames, 0, True)
	await message.reply(messages.PLAYERS_ONLINE, reply_markup=new_markup)


@server_router.message(Command("execute"))
async def execute_command(message: Message):
	if not rcon_handler.is_configured:
		await message.reply(messages.FEATURE_WAS_NOT_SETUP)
		return
	if message.from_user.id not in config.admins.ids:
		await message.reply(messages.PERMISSION_LEVEL_TOO_LOW)
		return
	data: list[str] = message.text.split(" ", 1)
	if len(data) == 1:
		await message.reply(
			messages.INCORRECT_RCON_COMMAND_FORMAT, parse_mode=ParseMode.MARKDOWN_V2
		)
		return
	response: str = await rcon_handler.execute(data[1])
	if response is None:
		response = messages.GENERAL_FAILURE
	elif response == "":
		response = messages.COMMAND_EXECUTED_SUCCESSFULLY
	await message.reply(f"```Server\n{response}```", parse_mode=ParseMode.MARKDOWN_V2)
