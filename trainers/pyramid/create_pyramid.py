from PIL import Image, ImageDraw, ImageFont
import random


def created_img():
    """Тут содаётся белый фон для пирамиды"""
    img = Image.new('RGBA', (400, 300), 'white')
    return img


def sorted_words():
    """Тут мы отсеиваем подходящие слова из файла"""
    words = []
    with open('trainers/pyramid/word_rus.txt', 'r') as file:
        for line in file:
            if len(line.strip()) == 4:
                words.append(line.strip())
    return words
    

def format_word():
    """Из колекции слов выбираем случайные 5 штук и форматируем их для пирамиды,
     делим по полам, вставляем пробелы, и по центру разделитель"""
    num = 2
    formated_text = []
    # Выбираем случайные слова пять штук
    words = random.sample(sorted_words(), 5)
    for word in words:
        space = " " * num
        formated_text.append(f"{word[:2]}{space}*{space}{word[2:]}")
        num = num + 3
    return formated_text


def create_pyramid():
    """Строим из полученых слов пирамиду"""
    #Создаём новое изображение 
    img = created_img()
    # Чтобы пирамида была ровной используем свободный моноширный шрифт
    font = ImageFont.truetype('font/Fira_Code/static/FiraCode-Regular.ttf', 18)
    # Получаем размер изображения на котором будет строится пирамида
    W,H = img.size
    # Переменая для отсупов между словами по высоте
    space = 0
    text = format_word()
    for word in text:
        # Получаем размер слова
        w,h = font.getsize(word)
        #добавляем отступ
        space = space + 40
        idraw = ImageDraw.Draw(img)
        idraw.text(
            ((W-w)/2, space),
            word,
            font=font,
            fill=('#000000'),
            )
    #Сохраняем получившуюся картинку
    return img.save('images/pyramid.png')