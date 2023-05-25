import aiogram
from aiogram import Bot, Dispatcher, types
from db.model import DB
from .keyboards import *
from .admin import *


def init_handlers(dp: aiogram.Dispatcher, db: DB, cash_users: set, admins: list[int]):
    flags, stack = {}, {}
    for i in admins:
        flags[i] = ""
        stack[i] = []


    @dp.message_handler(commands=["start"])
    async def handler(message: types.Message):
        if message.from_user.id in admins:
            await message.answer(
                text="Админочка",
                reply_markup=admin()
            )
            return
        if message.from_user.id not in cash_users:
            await message.answer(
                text="Здравствуйте!\n" +
                     "Рад что Вы обратились ко мне. Вам доступен бесплатный тестовый доступ на 2 дня,\n" +
                     "хотите попробовать?",
                reply_markup=new_user()
            )
            cash_users.add(message.from_user.id)
            return
        await message.answer(text="Вы в главном меню", reply_markup=main_loby())

    @dp.message_handler(text='FAQ')
    async def user_handler(message: types.Message):
        await message.answer(text=faq())

    @dp.message_handler(text='Поддержка')
    async def user_handler(message: types.Message):
        await message.answer(text=support())

    @dp.message_handler(text='Инструкция')
    async def user_handler(message: types.Message):
        await message.answer(text=instruction())




    # admins
    @dp.message_handler(text='Добавить сервер')
    async def admin_handler(message: types.Message):
        if message.from_user.id in admins:
            await message.answer(text=server_example())
            flags[message.from_user.id] = "create_server"
            return

    @dp.message_handler(content_types=["text"])
    async def admin_handler(message: types.Message):
        if message.from_user.id in admins:
            text, fl = admin_example(flags, message, stack)
            if not fl:
                await message.answer(text=text)
            elif fl == "add_server":
                db.add_server(*stack[message.from_user.id])
                await  message.answer(text="Успешно добавлен")