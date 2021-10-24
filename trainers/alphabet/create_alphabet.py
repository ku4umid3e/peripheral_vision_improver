import os
import random

from PIL import Image, ImageDraw, ImageFont

from settings import FONT_PATH, IMAGE_DIR

ALPHABET = list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")


def random_line(d):
    d.ellipse(
        (random.sample(range(50, 950, 100), 4)),
        fill='white',
        outline='black',
        )
    d.rectangle(
        random.sample(range(0, 1000, 100), 4),
        width=2,
        fill='white',
        outline='black'    
        )

    d.line(random.sample(range(0, 1000, 100), 4), width=3)

    d.polygon(
        (random.sample(range(50, 950, 100), 4)),
        fill='white',
        outline='black',
        )
    
    d.line((random.sample(range(50, 950, 100), 4)), width=2)


def _draw_letters(d):
    h_points = list(range(100, 900, 27))
    w_points = list(range(100, 900, 27))
    random.shuffle(h_points)
    random.shuffle(w_points)
    random.shuffle(ALPHABET)

    for let, h_point, w_point in zip(ALPHABET, h_points, w_points):
        _draw_letter(
            d,
            size_font=random.randint(50, 100),
            letter=let,
            point=(h_point, w_point)
        )
    missing_litters =(ALPHABET[-1], ALPHABET[-2], ALPHABET[-3])
    print(missing_litters)


def _draw_letter(d,
                 size_font,
                 letter,
                 point,
                 font=FONT_PATH,
                 color_font="black",
                 ):
    font = ImageFont.truetype(font, size_font)
    d.text(point, text=letter, fill=color_font, font=font)


def create_alphabet(size_by_side=1000, background="white"):
    img = Image.new('RGB', (size_by_side, size_by_side), color=background)
    d = ImageDraw.Draw(img)
    repeat = [random_line(d) for _ in range(5)]
    repeat
    _draw_letters(d)
    img.save(os.path.join(IMAGE_DIR, 'alphabet.png'))
    

if __name__ == '__main__':
    create_alphabet()
