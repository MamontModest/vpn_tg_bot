from aiogram import types


def admin() -> types.ReplyKeyboardMarkup:
    builder = types.ReplyKeyboardMarkup(resize_keyboard=True)
    builder.row(types.KeyboardButton(
        text="Тарифы",
        callback_data="tariffs")
    )
    builder.insert(types.KeyboardButton(
        text="Мой ключ",
        callback_data="mytarif")
    )
    builder.row(types.KeyboardButton(
        text="Поддержка",
        callback_data="support")
    )
    builder.insert(types.KeyboardButton(
        text="FAQ",
        callback_data="FAQ")
    )
    builder.insert(types.KeyboardButton(
        text="Инструкция",
        callback_data="instruction")
    )
    builder.row(types.KeyboardButton(
        text="Добавить сервер",
        callback_data="add_server")
    )
    return builder


def server_example() -> str:
    return "Заполни поля host=? username=? port=? password=?\n\n" \
           "Например \"host=127.0.0.1 username=root port=22 password=mypassword\"\n" \
           "Заметь имеется отсутствие пробелов между знаком \"=\""


def parse_server(message: str) -> [str, list[int]]:
    server = []
    for i in message.split():
        server.append(i.split("=")[1])

    return ["информация о сервере\n" + " ".join(server) + "\nВсё верно?", server]


def admin_example(flag, message: types.Message, stack) -> [str, str]:
    if flag[message.from_user.id] == "create_server":
        flag[message.from_user.id] = "complete_server"
        text, stack[message.from_user.id] = parse_server(message.text)
        return text, ""

    if flag[message.from_user.id] == "complete_server":
        if message.text.lower() == "да" or message.text.lower():
            print(stack[message.from_user.id])
            return "", "add_server"

    return "1"






