import sys
import asyncio
import logging

from src.buttons.router import buttons_router
from src.constants import DEV_MODE
from src.server.router import server_router
from src.bot import bot

from aiogram import Dispatcher


async def main() -> None:
    dp: Dispatcher = Dispatcher()
    dp.include_router(server_router)
    dp.include_router(buttons_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s |%(levelname)s| %(name)s: %(message)s',
        datefmt='%H:%M:%S %d.%m.%Y',
        level=logging.DEBUG if DEV_MODE else logging.INFO,
        stream=sys.stdout
    )
    asyncio.run(main())
