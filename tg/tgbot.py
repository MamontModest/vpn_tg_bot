import logging

import aiogram
import pika
from aiogram import Bot, Dispatcher, types
from db.model import DB
import tg.users as users
import tg.admin as admin


def init_handlers(dp: aiogram.Dispatcher, db: DB, cash_users: set, admins: list[int], channel: pika.connection.Connection.channel):
    flags, stack = {}, {}
    for i in admins:
        flags[i] = ""
        stack[i] = []

    @dp.message_handler(commands=["start"])
    @dp.message_handler(text="Главное меню")
    async def handler(message: types.Message):
        if message.from_user.id in admins:
            await message.answer(
                text="Админочка",
                reply_markup=admin.admin()
            )
        if message.from_user.id not in cash_users:
            await message.answer(
                text="Здравствуйте!\n" +
                     "Рад что Вы обратились ко мне. Вам доступен бесплатный тестовый доступ на 2 дня,\n" +
                     "хотите попробовать?",
                reply_markup=users.new_user()
            )
            return
        await message.answer(text="Вы в главном меню", reply_markup=users.main_loby())

    @dp.message_handler(text='FAQ')
    async def user_handler(message: types.Message):
        await message.answer(text=users.faq())

    @dp.message_handler(text='Поддержка')
    async def user_handler(message: types.Message):
        await message.answer(text=users.support())

    @dp.message_handler(text='Инструкция')
    async def user_handler(message: types.Message):
        await message.answer(text=users.instruction())

    # admins
    @dp.message_handler(text='Добавить сервер')
    async def admin_handler(message: types.Message):
        if message.from_user.id in admins:
            await message.answer(text=admin.server_example())
            flags[message.from_user.id] = "create_server"
            return
    # Тарифы + ключ
    @dp.message_handler(text='Тарифы')
    @dp.message_handler(text='Нет-хочу сразу купить тариф. 🇳🇱')
    async def admin_handler(message: types.Message):
        await message.answer(text="Выбирайте любой удобный вариант:", reply_markup=users.tariffs())

    @dp.message_handler(text="Мой ключ")
    async def admin_handler(message: types.Message):
        us = users.User(message.from_user.id)
        print(us)

    # пробный период
    @dp.message_handler(text="Да!")
    async def user_handler(message: types.Message):
        await message.answer(
            text="Супер, мой ВПН работает внутри приложения 'Outline'\nВам нужно его скачать, вот ссылки :",
            reply_markup=users.free_period_Inline())
        await message.answer(text="Если вы готовы, мы можем начать пробный период прямо сейчас",
                             reply_markup=users.free_period())

    @dp.message_handler(text="Хорошо скачал. Что далее?")
    async def user_handler(message: types.Message):
        pass






    @dp.message_handler(content_types=["text"])
    async def admin_handler(message: types.Message):
        if message.from_user.id in admins:
            text, fl = admin.admin_example(flags, message, stack)
            if not fl:
                await message.answer(text=text)
            elif fl == "add_server":
                channel.basic_publish(exchange="", routing_key="server", body=",".join(stack[message.from_user.id]))
                await message.answer(text="Успешно добавлен")

    print("tg_bot start")
