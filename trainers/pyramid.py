from PIL import Image, ImageDraw, ImageFont
import random

from settings import FONT_PATH


def created_img(image_width: int, image_height: int):
    """Тут создаётся белый фон для пирамиды"""
    img = Image.new('RGBA', (image_width, image_height), 'white')
    return img


def get_words(len_=4):
    """Тут мы отсеиваем подходящие слова из файла"""
    with open('trainers/word_for_pyramid.txt', 'r', encoding='utf-8') as file:
        return [str.strip(word) for word in file.readlines() if len(str.strip(word)) == len_]


def format_word(number):
    """Из коллекции слов выбираем случайные слова и форматируем их для
    пирамиды, делим по полам, вставляем пробелы, и по центру
    разделитель"""
    num = 2
    formatted_text = []
    # Выбираем случайные слова пять штук
    words = get_words()
    random.shuffle(words)
    words = words[:number]
    for word in words:
        space = " " * num
        formatted_text.append(f"{word[:2]}{space}*{space}{word[2:]}")
        num = num + 3
    return formatted_text


def create_pyramid(height):
    """Строим из полученных слов пирамиду"""
    # Получаем размер изображения на котором будет строится пирамида
    image_width = 100 + 65 * height
    image_height = 22 * height + 40
    # Создаём новое изображение
    img = created_img(image_width, image_height)
    # Чтобы пирамида была ровной используем свободный моноширинный шрифт
    font = ImageFont.truetype(FONT_PATH, 18)
    # Переменная для отступов между словами по высоте
    space = 0
    text = format_word(height)
    for word in text:
        # Получаем размер слова
        word_width, word_height = font.getsize(word)
        # добавляем отступ
        space = space + 25
        idraw = ImageDraw.Draw(img)
        idraw.text(
            ((image_width - word_width) / 2, space - (word_height / 2)),
            word,
            font=font,
            fill=('#000000'),
        )
    # Сохраняем получившуюся картинку
    return img.save('images/pyramid.png')
