"""
--- Day 2: I Was Told There Would Be No Math ---
The elves are running low on wrapping paper, and so they need to submit an order for more. 
They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.

Fortunately, every present is a box (a perfect right rectangular prism), 
which makes calculating the required wrapping paper for each gift a little easier: 
find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. 
The elves also need a little extra paper for each present: the area of the smallest side.

For example:

A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.
All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?
"""

# input sanitation
with open("2015/python/day02/input.txt", "r") as fp:
    lines = fp.readlines()

presents_dimensions = []
for i, line in enumerate(lines, start=1):
    potential_dimensions = line.split(sep="x")
    if len(potential_dimensions) != 3:
        print(f"Line {i} has wrong number of dimensions")

    int_dimensions = [int(d) for d in potential_dimensions]
    presents_dimensions.append(int_dimensions)

area = 0
for l, w, h in presents_dimensions:
    a = 2*l*w + 2*w*h + 2*h*l
    lw = l*w
    wh = w*h
    hl = h*l
    min_da = min(lw, wh, hl)
    a_with_extra = a + min_da
    area += a_with_extra

print(f"{area = }")

