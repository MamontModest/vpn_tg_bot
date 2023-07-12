from aiogram import types

import db.model


class User:
    def __init__(self, uid, key=None, data=None, free=False):
        self.uid = uid
        self.key = key
        self.data = data
        self.free = free

    def upload_user(self, database: db.model.DB):
        cur = database.conn.cursor()
        query = """SELECT (key, data, free) FROM USERS where uid=$1"""
        cur.execute(query, self.uid)
        tp = cur.fetchone()
        self.key, self.data, self.free = tp[0], tp[1], tp[2]
        database.conn.commit()
        cur.close()
    def create_user(self, database: db.model.DB):


























        cur = database.conn.cursor()
        query = """INSERT INTO USERS (uid, vpn_key_id, vpn_key, datetime, free) values($1, $2, $3, $4, $5)"""
        cur.execute(query, self.uid, None, None, None, True)
        database.conn.commit()
        cur.close()

    def __str__(self):
        return str(self.uid) + self.key + self.data + self.free


def new_user() -> types.ReplyKeyboardMarkup:
    builder = types.ReplyKeyboardMarkup()
    builder.add(types.KeyboardButton(
        text="Да!"))
    builder.add(types.KeyboardButton(
        text='Нет-хочу сразу купить тариф. 🇳🇱'))
    return builder


def main_loby() -> types.ReplyKeyboardMarkup:
    builder = types.ReplyKeyboardMarkup(resize_keyboard=True)
    builder.row(types.KeyboardButton(
        text="Тарифы"
    ))
    builder.insert(types.KeyboardButton(
        text="Мой ключ"
    ))
    builder.row(types.KeyboardButton(
        text="Поддержка"
    ))
    builder.insert(types.KeyboardButton(
        text="FAQ"
    ))
    builder.insert(types.KeyboardButton(
        text="Инструкция\n"
    ))
    return builder


def tariffs() -> types.ReplyKeyboardMarkup:
    builder = types.ReplyKeyboardMarkup(resize_keyboard=True)
    builder.row(types.KeyboardButton(
        text="Месяц - 149 рублей"
    ))
    builder.insert(types.KeyboardButton(
        text="3 Месяца - 349 рублей"
    ))
    builder.row(types.KeyboardButton(
        text="Целый год - 999 рублей"
    ))
    builder.insert(types.KeyboardButton(
        text="Главное меню"
    ))
    return builder

def free_period_Inline() -> types.InlineKeyboardMarkup:
    builder = types.InlineKeyboardMarkup(resize_keyboard=True)
    builder.row(
        types.KeyboardButton(
            text="App Store",
            url='https://apps.apple.com/us/app/outline-app/id1356177741'),
        types.KeyboardButton(
            text="Play Market",
            url='https://play.google.com/store/apps/details?id=org.outline.android.client&hl=en&gl=US')
    )
    return builder


def free_period() -> types.ReplyKeyboardMarkup:
    builder = types.ReplyKeyboardMarkup(resize_keyboard=True)
    builder.row(
        types.KeyboardButton(
            text="Хорошо скачал. Что далее?",
        ),
        types.KeyboardButton(
            text="Главное меню",
        )
    )
    return builder

def faq() -> str:
    return "Что такое 𝓥𝓟𝓝 и зачем оно мне?\n" \
           "VPN это виртуальная частная сеть которая, используя цифровой туннель," \
           " «переносит» вас в ту страну, где находится сервер VPN." \
           "В нашем случае это Россия. Нужно это бывает в случаях когда внутри вашей страны некоторые сайты не работают.\n" \
           "Получил ссылку. Дальше что?\n" \
           "Ссылка это и есть ваш персональный ключ, который подключает вас к нашему серверу  RU VPN." \
           "Если вы сделали всё по инструкции то включение и выключение RU VPN будет происходить через приложение Outline" \
           "нажатием одной кнопки подключить / отключить.\n" \
           "Как проверить работает ли VPN?\n" \
           "Можете открыть сайт 2ip.ru и посмотреть в какой стране вас видит сайт. Должно быть написано Россия.\n" \
           "Если у вас остались вопросы пишите сюда: @gkorkots)"


def support() -> str:
    return "Перед тем как задать вопрос, обязательно прочитайте подробную инструкцию и раздел FAQ." \
           "Для ускорения решения технических вопросов, можете сразу прислать скриншот с открытым приложением" \
           " Outline и сообщение от бота из раздела \"Мой ключ\"." \
           "Ваши вопросы и обращения направлять сюда @gkorkots "


def instruction() -> str:
    return """1. Скачайте и установите на устройство приложение Outline:

        iOS: https://itunes.apple.com/app/outline-app/id1356177741
        macOS: https://itunes.apple.com/app/outline-app/id1356178125
        Windows: https://s3.amazonaws.com/outline-releases/client/windows/stable/Outline-Client.exe
        Linux: https://s3.amazonaws.com/outline-releases/client/linux/stable/Outline-Client.AppImage
        Android: https://play.google.com/store/apps/details?id=org.outline.android.client
        Дополнительная ссылка для Android: https://s3.amazonaws.com/outline-releases/client/android/stable/Outline-Client.apk

        2. Получите ключ доступа, который начинается с ss://, а затем скопируйте его.

        3. Откройте клиент Outline. Если ваш ключ доступа определился автоматически, нажмите "Подключиться". Если этого не произошло, вставьте ключ в поле и нажмите "Подключиться".

        Теперь у вас есть доступ к свободному интернету. Чтобы убедиться, что вы подключились к серверу, введите в Google Поиске фразу "Какой у меня IP-адрес". IP-адрес, указанный в Google, должен совпадать с IP-адресом в клиенте Outline.

        Дополнительные сведения можно найти на странице https://getoutline.org/."""


