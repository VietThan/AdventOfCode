"""
--- Day 5: Doesn't He Have Intern-Elves For This? ---
Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

1. It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
2. It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
3. It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

For example:

1. ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...),
   and none of the disallowed substrings.
2. aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
3. jchzalrnumimnmhp is naughty because it has no double letter.
4. haegwjzuvuyypxyu is naughty because it contains the string xy.
5. dvszwmarrgswjxmb is naughty because it contains only one vowel.

How many strings are nice?
"""


import pathlib
current_dir = pathlib.Path(__file__).parent.resolve()

input_filepath = current_dir / "input.txt"

with open(input_filepath, "r") as fp:
    lines = fp.readlines()


BAD_COMBO = {
    "b" : "a",
    "d" : "c",
    "q" : "p",
    "y" : "x"
}

def is_nice(string: str) -> bool:
    # setup
    vowels_count = {
        "a" : 0,
        "e" : 0,
        "i" : 0,
        "o" : 0,
        "u" : 0
    }
    has_double = False

    c_prev = None
    i = 0

    n = len(string)

    while (i < n):
        c = string[i]

        if c in vowels_count:
            vowels_count[c] += 1

        if c == c_prev:
            has_double = True

        if c in BAD_COMBO and BAD_COMBO[c] == c_prev:
            return False

        c_prev = c
        i += 1

    vowels_counts_total = sum(vowels_count.values())

    if vowels_counts_total >= 3 and has_double:
        return True
    
    return False

# lines = [
#     "ugknbfddgicrmopn",
#     "aaa",
#     "jchzalrnumimnmhp",
#     "haegwjzuvuyypxyu",
#     "dvszwmarrgswjxmb"
# ]  


nice_lines: list[str] = []
naughty_lines: list[str] = []
for line in lines:
    if is_nice(string=line):
        nice_lines.append(line)
    else:
        naughty_lines.append(line)

print (f"{len(nice_lines)} nice lines")
print (f"{len(naughty_lines)} naughty lines")


