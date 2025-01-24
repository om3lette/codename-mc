from python.bots.telegram.src.constants import config
from python.bots.telegram.src.response_messages import PING_ERROR_MESSAGE, PING_HANGUP_MESSAGE, PING_HANGUP_ADMIN_MESSAGE, NO_ADMINS_FOUND_MESSAGE

from aiogram.types import Message
from aiogram.exceptions import TelegramForbiddenError
from python.bots.telegram.src.bot import bot


async def default_ping_error_callback(request_message: Message, attempt_number: int, is_attempt_final: bool = False):
    await request_message.answer(
        PING_ERROR_MESSAGE.format(
            attempt_number=attempt_number,
            time_before_retry=config.connection.seconds_between_retries
        )
    )
    if not is_attempt_final:
        return
    admin_usernames_text: str = ", ".join(f"@{admin_username}" for admin_username in config.admins.usernames)
    await request_message.reply(PING_HANGUP_MESSAGE.format(admins=admin_usernames_text or NO_ADMINS_FOUND_MESSAGE))

    # Notify admins
    for admin_id in config.admins.ids:
        try:
            await bot.send_message(admin_id, PING_HANGUP_ADMIN_MESSAGE.format(server_name=config.server.name))
        except TelegramForbiddenError:
            pass
