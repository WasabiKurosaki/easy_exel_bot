import logging
import asyncio
import os
from dotenv import load_dotenv
import sys
import utils

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

dp = Dispatcher()

# init db


async def main() -> None:

    load_dotenv()
    DOWNLOAD_DIR = os.getenv('DOWNLOAD_DIR')
    API_TOKEN = os.getenv('API_TOKEN')

    # Initialize bot and dispatcher
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher(bot)

    utils.init_dir(DOWNLOAD_DIR)

    # And the run events dispatching
    await dp.start_polling(bot)



@dp.message_handler(content_types=['photo', 'document'])
async def exel_handler(message: types.Message):
    print(123123)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
