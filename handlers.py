import os

from settings import IMAGE_DIR
from trainers.shulte import create_tables
from common.keyboards import get_keyboard, options_shulte
from trainers.pyramid import create_pyramid
from utilites.utilites import get_emoji


def greet_user(update, context):
    username = update.effective_user.first_name
    context.user_data['emoji'] = get_emoji(context.user_data)
    text = f"Здравствуй, пользователь {username} {context.user_data['emoji']}! " \
           f"Это бот для тренировки периферийного зрения и памяти! " \
           f"Выбери упражнение"
    update.message.reply_text(text, reply_markup=get_keyboard())


def talk_to_me(update, context):
    context.user_data['emoji'] = get_emoji(context.user_data)
    username = update.effective_user.first_name
    text = update.message.text
    update.message.reply_text(f"Здравствуй, {username} {context.user_data['emoji']}! Ты написал: {text}",
                              reply_markup=get_keyboard())


def send_shulte(update, context):
    update.callback_query.answer()
    cnt_cells = int(update.callback_query.data)
    text = f"Создаю таблицу {update.callback_query.data} на {update.callback_query.data}"
    update.callback_query.edit_message_text(text=text)
    path_to_pict = None
    chat_id = update.effective_chat.id
    create_tables(cnt_cells)

    path_to_pict = os.path.join(IMAGE_DIR, "shulte.png")

    context.bot.send_photo(chat_id=chat_id, photo=open(path_to_pict, 'rb'))


def send_pyramid(update, context):
    # Пробуем получить число из сообщения, если не получится отправим запрос на 5 слов
    height = int(update.message.text.split()[-1]) if update.message.text.split()[-1].isdigit() else 5
    create_pyramid(height)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(os.path.join(IMAGE_DIR, 'pyramid.png'), 'rb'))


def menu_shulte(update, context):
    update.message.reply_text("Выберете размер таблицы", reply_markup=options_shulte())
