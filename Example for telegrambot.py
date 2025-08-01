from aiogram import Bot, Dispatcher

import asyncio
import os



TOKEN = os.getenv("BOT_TOKEN")

async def main():
    print("Bot is on!")
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot is off")