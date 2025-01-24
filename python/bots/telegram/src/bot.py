from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from python.bots.telegram.src.constants import config

bot: Bot = Bot(token=config.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
