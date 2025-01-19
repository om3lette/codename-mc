import logging

from typing import Callable
from sys import exit

from src.constants import ExitStatus, ADMINS, ADMIN_IDS, SECONDS_BETWEEN_RETRIES, SERVER_NAME
from src.response_messages import PING_ERROR_MESSAGE, PING_HANGUP_MESSAGE, PING_HANGUP_ADMIN_MESSAGE, NO_ADMINS_FOUND_MESSAGE

from aiogram.types import Message
from aiogram.exceptions import TelegramForbiddenError
from src.bot import bot


def check_for_exit_condition(
        data: any,
        error_checker: Callable = lambda x: x,
        message: str = 'Critical error occurred. Aborting...',
        event_type: ExitStatus = ExitStatus.ERROR,
        error: str | None = None
) -> None:
    if not error_checker(data):
        return
    if event_type == ExitStatus.ERROR:
        logging.error(message)
    else:
        logging.info(message)

    if error:
        logging.critical(error)
    exit()


async def default_ping_error_callback(request_message: Message, attempt_number: int, is_attempt_final: bool = False):
    await request_message.answer(
        PING_ERROR_MESSAGE.format(
            attempt_number=attempt_number,
            time_before_retry=SECONDS_BETWEEN_RETRIES
        )
    )
    if not is_attempt_final:
        return
    await request_message.reply(PING_HANGUP_MESSAGE.format(admins=", ".join(ADMINS) or NO_ADMINS_FOUND_MESSAGE))

    # Notify admins
    for admin_id in ADMIN_IDS:
        try:
            await bot.send_message(admin_id, PING_HANGUP_ADMIN_MESSAGE.format(server_name=SERVER_NAME))
        except TelegramForbiddenError:
            pass
