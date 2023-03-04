from PIL import Image, ImageDraw, ImageFont
import random
from typing import Tuple

from settings import FONT_PATH


class ShulteTable:
    """Класс для создания таблицы Шульте"""

    def __init__(self, cell_size: int = 150, square_from_cells: int = 3):
        """Конструктор класса, принимает размер
        клетки и количество клеток по одной из сторон"""
        self.cell_size = cell_size
        self.square_from_cells = square_from_cells
        self.numbers = [str(i) for i in range(1, square_from_cells ** 2 + 1)]
        random.shuffle(self.numbers)

    def get_image_size(self) -> Tuple[int, int]:
        """Метод класса, вычисляющий размер изображения"""
        return (self.cell_size * self.square_from_cells, self.cell_size * self.square_from_cells)

    def draw_cells(self, drawer: ImageDraw.Draw):
        """Метод класса, рисующий клетки таблицы"""
        for x in range(0, self.square_from_cells * self.cell_size, self.cell_size):
            for y in range(0, self.square_from_cells * self.cell_size, self.cell_size):
                drawer.rectangle((x, y, x + self.cell_size, y + self.cell_size), outline="black", width=1)

    def draw_numbers(self, drawer: ImageDraw.Draw, font: ImageFont):
        """Метод класса, расставляющий цифры"""
        count = 0
        for x in range(0, self.square_from_cells * self.cell_size, self.cell_size):
            if len(self.numbers) == 0:
                break
            for y in range(0, self.square_from_cells * self.cell_size, self.cell_size):
                if count < self.square_from_cells:
                    count += 1
                    number = self.numbers.pop()
                    text_width, text_height = drawer.textsize(number, font=font)
                    text_x = x + self.cell_size / 2
                    text_y = y + self.cell_size / 2
                    drawer.text((text_x, text_y), text=number, fill="black", font=font, anchor="mm")
            count = 0

    def create_table_image(self):
        """Метод класса, создающий изображение таблицы"""
        image = Image.new('RGB', self.get_image_size(), color="white")
        drawer = ImageDraw.Draw(image)
        font = ImageFont.truetype(FONT_PATH, 50)
        self.draw_cells(drawer)
        self.draw_numbers(drawer, font)
        return image

    def save_table_image(self, path: str = 'images/shulte.png'):
        """Метод класса, сохраняющий изображение таблицы"""
        self.create_table_image().save(path)


def create_tables(cells: int):
    """Функция для создания экземпляра класса ShulteTable с необходимым количеством клеток/цифр"""
    table = ShulteTable(square_from_cells=cells)
    table.save_table_image()
