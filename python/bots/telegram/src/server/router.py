from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.enums import ParseMode
from mcstatus.status_response import JavaStatusPlayers

from python.bots.telegram.src.buttons.builders import players_markup_builder
from python.bots.telegram.src.constants import ADMIN_IDS
from python.bots.telegram.src.handlers import connection_handler, rcon_handler
from python.bots.telegram.src.response_messages import *

server_router: Router = Router()


@server_router.message(Command("is_alive"))
async def check_server_status(message: Message):
    [is_alive, response_time] = await connection_handler.execute(message, connection_handler.connection.async_ping)
    if not is_alive:
        return
    await message.reply(PING_SUCCESS_MESSAGE.format(latency=round(response_time, 2)))


@server_router.message(Command("current_online"))
async def players_number(message: Message):
    [is_alive, status] = await connection_handler.execute(message, connection_handler.get_server_status)
    if not is_alive:
        return
    players: JavaStatusPlayers = status.players
    await message.reply(PLAYERS_NUMBER_MESSAGE.format(current_number=players.online, capacity=players.max))


@server_router.message(Command("players_online"))
async def players_list(message: Message):
    [is_alive, server_status] = await connection_handler.execute(message, connection_handler.get_server_status)
    if not is_alive:
        return
    players: JavaStatusPlayers = server_status.players
    if players.sample is None or len(players.sample) == 0:
        await message.reply(PLAYERS_ONLINE_MESSAGE + '\n' + NO_PLAYERS_ONLINE_MESSAGE)
        return
    usernames: list[str] = [player.name for player in players.sample]
    new_markup, exit_status = players_markup_builder.build(usernames, 0, True)
    await message.reply(PLAYERS_ONLINE_MESSAGE, reply_markup=new_markup)


@server_router.message(Command("execute"))
async def execute_command(message: Message):
    if not rcon_handler.is_configured:
        await message.reply(FEATURE_WAS_NOT_SETUP_MESSAGE)
        return
    if message.from_user.id not in ADMIN_IDS:
        await message.reply(PERMISSION_LEVEL_TOO_LOW_MESSAGE)
        return
    data: list[str] = message.text.split(' ', 1)
    if len(data) == 1:
        await message.reply(INCORRECT_RCON_COMMAND_FORMAT_MESSAGE, parse_mode=ParseMode.MARKDOWN_V2)
        return
    response: str = await rcon_handler.execute(data[1])
    if response is None:
        response = GENERAL_FAILURE_MESSAGE
    elif response == "":
        response = COMMAND_EXECUTED_SUCCESSFULLY_MESSAGE
    await message.reply(f"```Server\n{response}```", parse_mode=ParseMode.MARKDOWN_V2)
