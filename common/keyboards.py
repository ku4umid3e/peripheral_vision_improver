from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


def get_keyboard():
    return ReplyKeyboardMarkup([["Шульте", "Алфавит", "Пирамида"]], resize_keyboard=True)

def options_shulte():
    keyboard =  [
        [
        InlineKeyboardButton("Три на Три", callback_data='3'),
        InlineKeyboardButton("Пять на Пять", callback_data='5'),
        InlineKeyboardButton("Семь на Семь", callback_data='7')
        ]
    ]
    return InlineKeyboardMarkup(keyboard)
    