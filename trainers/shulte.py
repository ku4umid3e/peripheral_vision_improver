import random

from PIL import Image, ImageDraw, ImageFont

from settings import FONT_PATH

_coordinate_lines_3_x_3 = [
    (0, 150, 450, 150),
    (0, 300, 450, 300),
    (150, 0, 150, 450),
    (300, 0, 300, 450)
]

_coordinate_lines_5_x_5 = [
    (0, 150, 750, 150),
    (0, 300, 750, 300),
    (0, 450, 750, 450),
    (0, 600, 750, 600),
    (150, 0, 150, 750),
    (300, 0, 300, 750),
    (450, 0, 450, 750),
    (600, 0, 600, 750)
]

_coordinate_lines_7_x_7 = [
    (0, 150, 1050, 150),
    (0, 300, 1050, 300),
    (0, 450, 1050, 450),
    (0, 600, 1050, 600),
    (0, 750, 1050, 750),
    (0, 900, 1050, 900),
    (150, 0, 150, 1050),
    (300, 0, 300, 1050),
    (450, 0, 450, 1050),
    (600, 0, 600, 1050),
    (750, 0, 750, 1050),
    (900, 0, 900, 1050)
]


def _get_odd_list(len_: int) -> list:
    cnt = 1
    result = list()
    while True:
        if cnt % 2:
            result.append(cnt)
        if len(result) == len_:
            return result
        cnt += 1


def _get_steps(num_by_side: int) -> list:
    return _get_odd_list(num_by_side)


def _get_line_coordinates(num_by_side: int) -> list:
    if num_by_side == 3:
        return _coordinate_lines_3_x_3
    elif num_by_side == 5:
        return _coordinate_lines_5_x_5
    elif num_by_side == 7:
        return _coordinate_lines_7_x_7
    else:
        raise RuntimeError(f'Количество ячеек {num_by_side} не поддерживается')


def _draw_cell(d, coordinate_lines, size_rectangle, color="black", width=5):
    d.rectangle((0, 0, size_rectangle, size_rectangle), outline=color, width=width * 3)
    for coord in coordinate_lines:
        d.line(coord, fill=color, width=width)


def _draw_num(d,
              size_step: int,
              steps: list,
              size_font=50,
              font=FONT_PATH,
              color_font="black",
              middle_color="red"):
    font = ImageFont.truetype(font, size_font)
    points = list()
    for p_1 in steps:
        for p_2 in steps:
            points.append(((size_step * p_1) / 2, (size_step * p_2) / 2))

    nums = [str(i) for i in range(1, sum(steps) + 1)]
    random.shuffle(nums)
    middle_elem = nums[int(len(nums) / 2)]
    for point, num in zip(points, nums):
        if num == middle_elem:
            d.text(point, text=num, fill=middle_color, font=font, anchor="mm")
            continue
        d.text(point, text=num, fill=color_font, font=font, anchor="mm")


def create_(num_by_side, size_by_side, background="white"):
    img = Image.new('RGB', (size_by_side, size_by_side), color=background)
    d = ImageDraw.Draw(img)
    coordinate_lines = _get_line_coordinates(num_by_side)
    _draw_cell(d, coordinate_lines, size_by_side)
    size_by_side_cell = size_by_side / num_by_side
    steps = _get_steps(num_by_side)
    _draw_num(d, size_by_side_cell, steps)
    img.save(f'images/shulte_{num_by_side}_x_{num_by_side}.png')


def create_all_tables():
    create_(num_by_side=3, size_by_side=450)
    create_(num_by_side=5, size_by_side=750)
    create_(num_by_side=7, size_by_side=1050)
