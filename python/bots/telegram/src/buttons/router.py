from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram import F

from python.bots.telegram.src.buttons.builders import players_markup_builder
from python.bots.telegram.src.buttons.schemas import PaginationNav
from python.bots.telegram.src.buttons.services import PaginatorExitStatus
from python.bots.telegram.src.handlers import connection_handler
from python.bots.telegram.src.response_messages import PLAYERS_ONLINE, NO_PLAYERS_ONLINE

buttons_router: Router = Router()


@buttons_router.callback_query(F.data == "skip")
async def handle_navigation_no_action(call: CallbackQuery):
	await call.answer()


@buttons_router.callback_query(PaginationNav.filter())
async def handle_navigation(call: CallbackQuery, callback_data: PaginationNav):
	[is_alive, server_status] = await connection_handler.execute(
		call.message, connection_handler.get_server_status
	)
	if not is_alive:
		return
	if server_status.players.sample is None:
		await call.message.edit_text(PLAYERS_ONLINE + "\n" + NO_PLAYERS_ONLINE)
		await call.message.edit_reply_markup(reply_markup=None)
		return
	usernames: list[str] = [player.name for player in server_status.players.sample]
	new_markup, exit_status = players_markup_builder.build(
		usernames, callback_data.page
	)
	if exit_status == PaginatorExitStatus.ALREADY_UP_TO_DATE:
		await call.answer()
		return
	await call.message.edit_reply_markup(reply_markup=new_markup)
