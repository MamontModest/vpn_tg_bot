import asyncio
import time

import psycopg2
import os
import pika
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from db import model
from tg.tgbot import init_handlers

load_dotenv()

# broker
broker = os.environ.get("BROKER")

# bd
user = os.environ.get("USER")
db_name = os.environ.get("DB_NAME")
host = os.getenv("HOST")
password = os.environ.get("PASSWORD")
port = os.getenv("PORT")
db = model.DB(db_name, host, int(port), user, password)

# init db
db.create_databases()
cash_users = db.select_all_user()

# bot
token = os.getenv("TOKEN")
bot = Bot(token=token)
dp = Dispatcher(bot)

# admins
admins = list(map(int, os.getenv("admins").split(",")))

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue="keys")
channel.queue_declare(queue="server")

async def f():
    while True:
        print(1)
        await asyncio.sleep(10)

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    init_handlers(dp, db, cash_users, admins, channel)
    ioloop = asyncio.get_event_loop()
    tasks = [
        ioloop.create_task(main()),
        ioloop.create_task(f())
    ]
    ioloop.run_until_complete(asyncio.wait(tasks))
