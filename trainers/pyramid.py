from PIL import Image, ImageDraw, ImageFont
import random

from settings import FONT_PATH

def created_img(W: int, H: int):
    """Тут содаётся белый фон для пирамиды"""
    img = Image.new('RGBA', (W, H), 'white')
    return img


def get_words(len_=4):
    """Тут мы отсеиваем подходящие слова из файла"""
    with open('trainers/word_for_pyramid.txt', 'r', encoding='utf-8') as file:
        return [str.strip(word) for word in file.readlines() if len(str.strip(word)) == len_]


def format_word(number):
    """Из колекции слов выбираем случайные слова и форматируем их для пирамиды,
     делим по полам, вставляем пробелы, и по центру разделитель"""
    num = 2
    formated_text = []
    # Выбираем случайные слова пять штук
    words = get_words()
    random.shuffle(words)
    words = words[:number]
    # words = random.sample(sorted_words(), number)
    for word in words:
        space = " " * num
        formated_text.append(f"{word[:2]}{space}*{space}{word[2:]}")
        num = num + 3
    return formated_text


def create_pyramid(height):
    """Строим из полученых слов пирамиду"""
    # Получаем размер изображения на котором будет строится пирамида
    W = 100 + 65 * height
    H = 22 * height + 40
    # Создаём новое изображение
    img = created_img(W, H)
    # Чтобы пирамида была ровной используем свободный моноширный шрифт
    font = ImageFont.truetype(FONT_PATH, 18)
    # Переменая для отсупов между словами по высоте
    space = 0
    text = format_word(height)
    for word in text:
        # Получаем размер слова
        w, h = font.getsize(word)
        # добавляем отступ
        space = space + 25
        idraw = ImageDraw.Draw(img)
        idraw.text(
            ((W - w) / 2, space - (h / 2)),
            word,
            font=font,
            fill=('#000000'),
        )
    # Сохраняем получившуюся картинку
    return img.save('images/pyramid.png')
