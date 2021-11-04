import os
from posixpath import split
import random
import collections
import datetime

from PIL import Image, ImageDraw, ImageFont
from telegram import ReplyKeyboardRemove
from telegram.ext import ConversationHandler

from common.keyboards import get_keyboard
from settings import FONT_PATH, IMAGE_DIR


def random_line(d):
    d.rectangle(
       (random.sample(range(10, 990, 100), 4)),
       width=2,
       fill='white',
       outline='black'    
       )

    d.line((random.sample(range(10, 990, 100), 4)), width=3)

    d.polygon(
       (random.sample(range(10, 990, 100), 4)),
       fill='white',
       outline='black',
       )
   
    d.ellipse(
       random.sample(range(150, 900, 100), 4),
       fill='white',
       outline='black',
       )

    d.line((random.sample(range(10, 990, 100), 4)), width=2)


def to_shuffle_alphabet():
    ALPHABET = list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
    missing_litters = []
    random.shuffle(ALPHABET)
    repeat = [missing_litters.append(ALPHABET.pop()) for _ in range(3)]
    repeat
    return [ALPHABET, missing_litters]


def create_letter(letters, d):

    position_letter_in_height = list(random.sample(range(20, 900, 27), 30))
    position_letter_in_width = list(random.sample(range(20, 900, 27), 30))
    
    for letter, position_letter_in_height, position_letter_in_width in zip(letters, position_letter_in_height, position_letter_in_width):
        _draw_letter(d,
                size_font=random.randint(50, 100),
                letter=letter,
                point=(position_letter_in_height, position_letter_in_width)
                )


def _draw_letter(d,
                size_font,
                letter,
                point,
                font=FONT_PATH,
                color_font="black",
                ):
    font = ImageFont.truetype(font, size_font)
    d.text(point, text=letter, fill=color_font, font=font)
    size_letter = font.getsize(letter)
    return size_letter    


def create_alphabet():
    img = Image.new('RGB', (1000, 1000), color='white')
    draw = ImageDraw.Draw(img)
    repeat = [random_line(draw) for _ in range(5)]
    repeat
    abc = to_shuffle_alphabet()
    print(abc[1])
    create_letter(abc[0], draw)
    img.save(os.path.join(IMAGE_DIR, 'alphabet.png'))
    return abc[1]


def start_alphabet(update, context):
    update.message.reply_text(
            "Отличный выбор!\nПосмотри на картинку, найди и отправь мне отсутствующие три буквы.\n",
            reply_markup=ReplyKeyboardRemove()
            )
    chat_id = update.effective_chat.id
    context.user_data['start_time'] = datetime.datetime.now()
    context.user_data['question'] = create_alphabet()
    context.bot.send_photo(chat_id=chat_id, photo=open(os.path.join(IMAGE_DIR, 'alphabet.png'), 'rb'))
    return 'user_letters'
    

def check_letters(update, context):
    answer = update.message.text.lower().split()
    if len(answer) != 3:
        update.message.reply_text(f"Я не могу разобрать что ты написал: {answer}\nПожалуйста мне нужно только три буквы через пробел")
        return 'user_letters'

    elif collections.Counter(answer) != collections.Counter(context.user_data['question']):
        update.message.reply_text("Не верно. Попробуй еще раз")
        return 'user_letters'

    collections.Counter(answer) == collections.Counter(context.user_data['question'])
    search_time = datetime.datetime.now() - context.user_data['start_time']
    h, m, s = time_to_hours_minutes_seconds(search_time)
    update.message.reply_text(f"Верно. \nНа поиск ответа тебе потребовалось времени:\n {h}ч. {m}м. {s}с. ", reply_markup=get_keyboard())
    return ConversationHandler.END


def cancel(update, context):
    update.message.reply_text(
        'Может в следующий раз', 
        reply_markup=get_keyboard()
    )
    return ConversationHandler.END


def time_to_hours_minutes_seconds(duration):
    days, seconds = duration.days, duration.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 60)
    return hours, minutes, seconds


if __name__ == '__main__':
    create_alphabet()
