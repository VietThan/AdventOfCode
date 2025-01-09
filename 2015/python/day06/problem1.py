"""
--- Day 6: Probably a Fire Hazard ---
Because your neighbors keep defeating you in the holiday house decorating contest
year after year, you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you
instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at
each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether
to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs.
Each coordinate pair represents opposite corners of a rectangle, inclusive; a
coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square.
The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by
doing the instructions Santa sent you in order.

For example:

1. turn on 0,0 through 999,999 would turn on (or leave on) every light.
2. toggle 0,0 through 999,0 would toggle the first line of 1000 lights,
   turning off the ones that were on, and turning on the ones that were off.
3. turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.

After following the instructions, how many lights are lit?
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
    toggle_grid = create_toggle_grid(
        x_bot=x_bot,
        y_bot=y_bot,
        x_top=x_top,
        y_top=y_top
    )
    BASE_GRID ^= toggle_grid

def turn_off(x_bot: int, y_bot: int, x_top: int, y_top: int):
    global BASE_GRID
    for i in range(x_bot, x_top+1):
        for j in range(y_bot, y_top+1):
            BASE_GRID[i][j] = 0

def turn_on(x_bot: int, y_bot: int, x_top: int, y_top: int):
    global BASE_GRID
    for i in range(x_bot, x_top+1):
        for j in range(y_bot, y_top+1):
            BASE_GRID[i][j] = 1          




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
        if value == 0:
            continue
        elif value == 1:
            count += 1
        else:
            print(f"unexpected value {value} at {i = }, {j = }")

print(f"{count = }")


# print(BASE_GRID)
# toggle(0, 0, 1, 1)
# print(BASE_GRID)
# turn_off(1,1,1,1)
# print(BASE_GRID)
# turn_on(3,3,4,4)
# print(BASE_GRID)
# toggle(0,0,4,4)
# print(BASE_GRID)
# turn_off(0,2,1,3)
# print(BASE_GRID)