import asyncio
import psycopg2
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from db import model
from tg.tgbot import init_handlers
load_dotenv()

# bd
user = os.environ.get("USER")
db_name = os.environ.get("DB_NAME")
host = os.getenv("HOST")
password = os.environ.get("PASSWORD")
port = os.getenv("PORT")
db = model.DB(db_name, host, port, user, password)

# init db
db.create_databases()
cash_users = db.select_all_user()

# bot
token = os.getenv("TOKEN")
bot = Bot(token=token)
dp = Dispatcher(bot)

# admins
admins = list(map(int, os.getenv("admins").split(",")))

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    init_handlers(dp, db, cash_users, admins)
    asyncio.run(main())

