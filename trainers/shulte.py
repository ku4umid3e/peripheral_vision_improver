from PIL import Image, ImageDraw, ImageFont
import random

from settings import FONT_PATH



class Cell():
    """Этот клас создаёт поле клееток и в слцчайном порядке заполняет их цифрами"""
    def __init__(self, cell_size=150, square_from_cells=3):
        """Конструктор класса, принимает размер клетки и количество клеток по одной стороне"""
        self.cell_size = cell_size
        self.square_from_cells = square_from_cells


    def create_tables(self):
        """Метод класса, ничего не принимает, вычисляет размер необходимого изображения, рисует клетки, расставляет цифры. """
        image = Image.new('RGB', (self.cell_size * self.square_from_cells, self.cell_size * self.square_from_cells), color="white")
        drawer = ImageDraw.Draw(image)
        font = ImageFont.truetype(FONT_PATH, 50)
        numbers = [str(i) for i in range(1, self.square_from_cells **2 + 1)]
        random.shuffle(numbers)
        for coordinat_x in range(0, self.square_from_cells * self.cell_size + self.cell_size, self.cell_size):
            count = 0
            if len(numbers) == 0:
                for coordinat_y in range(0, self.square_from_cells * self.cell_size + self.cell_size, self.cell_size):
                    drawer.rectangle((coordinat_x , coordinat_y, self.cell_size, self.cell_size), outline="black", width=1)
                break
            for coordinat_y in range(0, self.square_from_cells * self.cell_size + self.cell_size, self.cell_size):
                drawer.rectangle((coordinat_x , coordinat_y, self.cell_size, self.cell_size), outline="black", width=1)
                if count < self.square_from_cells:
                    count += 1
                    drawer.text((coordinat_x + self.cell_size / 2, coordinat_y + self.cell_size / 2), text=str(numbers.pop()), fill="black", font=font, anchor="mm")
        image.save(f'images/shulte.png')


def create_tables(cells):
    """Создаём экземпляр класса с необходимым количеством клеток/цифр"""
    One_cell = Cell(square_from_cells=cells)
    One_cell.create_tables()
