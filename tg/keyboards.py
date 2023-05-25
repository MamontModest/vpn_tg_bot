from aiogram import types
def new_user()->types.InlineKeyboardMarkup:
    builder = types.InlineKeyboardMarkup()
    builder.add(types.InlineKeyboardButton(
        text="Да!",
        callback_data="try_yes")
    )
    builder.add(types.InlineKeyboardButton(
        text='Нет-хочу сразу купить тариф. 🇳🇱',
        callback_data='tariffs'))
    return builder

def main_loby()->types.ReplyKeyboardMarkup:
    builder = types.ReplyKeyboardMarkup(resize_keyboard=True)
    builder.row(types.KeyboardButton(
        text="Тарифы",
        callback_data="tariffs")
    )
    builder.insert(types.KeyboardButton(
        text="Мой ключ\n",
        callback_data="mytarif")
    )
    builder.row(types.KeyboardButton(
        text="Поддержка\n",
        callback_data="support")
    )
    builder.insert(types.KeyboardButton(
        text="FAQ\n",
        callback_data="FAQ")
    )
    builder.insert(types.KeyboardButton(
        text="Инструкция\n",
        callback_data="instruction")
    )
    return builder


def faq()->str:
    return "Что такое 𝓥𝓟𝓝 и зачем оно мне?\n"\
    "VPN это виртуальная частная сеть которая, используя цифровой туннель," \
    " «переносит» вас в ту страну, где находится сервер VPN."\
     "В нашем случае это Россия. Нужно это бывает в случаях когда внутри вашей страны некоторые сайты не работают.\n"\
    "Получил ссылку. Дальше что?\n"\
    "Ссылка это и есть ваш персональный ключ, который подключает вас к нашему серверу  RU VPN."\
    "Если вы сделали всё по инструкции то включение и выключение RU VPN будет происходить через приложение Outline"\
    "нажатием одной кнопки подключить / отключить.\n"\
    "Как проверить работает ли VPN?\n"\
    "Можете открыть сайт 2ip.ru и посмотреть в какой стране вас видит сайт. Должно быть написано Россия.\n"\
    "Если у вас остались вопросы пишите сюда: @gkorkots)"

def support()->str:
    return "Перед тем как задать вопрос, обязательно прочитайте подробную инструкцию и раздел FAQ."\
    "Для ускорения решения технических вопросов, можете сразу прислать скриншот с открытым приложением" \
           " Outline и сообщение от бота из раздела \"Мой ключ\"."\
    "Ваши вопросы и обращения направлять сюда @gkorkots "



def instruction()->str:
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