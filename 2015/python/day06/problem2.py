"""
--- Part Two ---
You just finish implementing your winning light pattern when you realize you mistranslated
Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; each light can have
a brightness of zero or more. The lights all start at zero.

1. The phrase turn on actually means that you should increase the brightness of those lights by 1.

2. The phrase turn off actually means that you should decrease the brightness of those lights by 1,
   to a minimum of zero.

3. The phrase toggle actually means that you should increase the brightness of those lights by 2.

What is the total brightness of all lights combined after following Santa's instructions?

For example:

turn on 0,0 through 0,0 would increase the total brightness by 1.
toggle 0,0 through 999,999 would increase the total brightness by 2000000.
"""

import numpy as np
import numpy.typing as npt
import pathlib
import re

N = 1000

def create_base_grid(default = 0) -> npt.NDArray:
    one_row = [default for _ in range(N)]
    all_rows = [one_row for _ in range(N)]

    return np.array(all_rows)

BASE_GRID = create_base_grid()


def create_grid(
    x_bot: int, 
    y_bot: int, 
    x_top: int, 
    y_top: int, 
    default = 0,
    variable = 1
) -> npt.NDArray:
    new_grid = create_base_grid(default=default)

    for i in range(x_bot, x_top+1):
        for j in range(y_bot, y_top+1):
            new_grid[i][j] = variable

    return new_grid


def create_toggle_grid(x_bot: int, y_bot: int, x_top: int, y_top: int) -> npt.NDArray:
    toggle_grid = create_grid(
        x_bot=x_bot,
        y_bot=y_bot,
        x_top=x_top,
        y_top=y_top,
        default=0,
        variable=1
    )
    return toggle_grid


def toggle(x_bot: int, y_bot: int, x_top: int, y_top: int):
    global BASE_GRID
    for i in range(x_bot, x_top+1):
        for j in range(y_bot, y_top+1):
            BASE_GRID[i][j] += 2

def turn_off(x_bot: int, y_bot: int, x_top: int, y_top: int):
    global BASE_GRID
    for i in range(x_bot, x_top+1):
        for j in range(y_bot, y_top+1):
            if BASE_GRID[i][j] > 0:
                BASE_GRID[i][j] -= 1

def turn_on(x_bot: int, y_bot: int, x_top: int, y_top: int):
    global BASE_GRID
    for i in range(x_bot, x_top+1):
        for j in range(y_bot, y_top+1):
            BASE_GRID[i][j] += 1          




current_dir = pathlib.Path(__file__).parent.resolve()

input_filepath = current_dir / "input.txt"

with open(input_filepath, "r") as fp:
    lines = fp.readlines()

# Regular expression pattern to match coordinates
pattern = r"(\d+,\d+)"


for line in lines:
    # Find all matches
    coordinates = re.findall(pattern, line)
    # Split the coordinates into tuples
    coordinate_pairs = [tuple(map(int, coord.split(','))) for coord in coordinates]

    x_bot, y_bot = coordinate_pairs[0]
    x_top, y_top = coordinate_pairs[1]

    if x_bot > x_top or y_bot > y_bot:
        print(f"something's wrong with: {line}")

    if line.startswith("turn on"):
        turn_on(x_bot, y_bot, x_top, y_top)
    if line.startswith("turn off"):
        turn_off(x_bot, y_bot, x_top, y_top)
    if line.startswith("toggle"):
        toggle(x_bot, y_bot, x_top, y_top)
        

count = 0

for i in range(N):
    for j in range(N):
        value = BASE_GRID[i][j]
        if value < 0 :
            print(f"Something wrong at {i = } {j = } : {value = }")

        count += int(value)

print(f"{count = }")