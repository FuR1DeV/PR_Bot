import os
from aiogram import Dispatcher, Bot
import logging
import asyncio

from commands import register_user_commands


async def main() -> None:
    logging.basicConfig(level=logging.DEBUG)
    dp = Dispatcher()
    bot = Bot(token=os.getenv("token"))

    register_user_commands(dp)

    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot stopped!")



