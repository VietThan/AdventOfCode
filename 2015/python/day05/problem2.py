"""
--- Part Two ---
Realizing the error of his ways, Santa has switched to a better model of
determining whether a string is naughty or nice. 
None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

1. It contains a pair of any two letters that appears at least twice 
   in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), 
   but not like aaa (aa, but it overlaps).
2. It contains at least one letter which repeats with exactly one letter
   between them, like xyx, abcdefeghi (efe), or even aaa.

For example:

1. qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj)
   and a letter that repeats with exactly one letter between them (zxz).
2. xxyxx is nice because it has a pair that appears twice and a letter
   that repeats with one between, even though the letters used by each rule overlap.
3. uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with 
   a single letter between them.
4. ieodomkazucvgmuy is naughty because it has a repeating letter with one 
   between (odo), but no pair that appears twice.

How many strings are nice under these new rules?
"""


import pathlib
current_dir = pathlib.Path(__file__).parent.resolve()

input_filepath = current_dir / "input.txt"

with open(input_filepath, "r") as fp:
    lines = fp.readlines()


def is_nice(string: str) -> bool:
    if len(string) < 5:
        return False

    # setup
    couples_index: dict[str, list[int]] = {}

    char_index: dict[str, list[int]] = {}



    c_prev = string[0]
    char_index[c_prev] = [0,]
    i = 1

    n = len(string)

    while i < n:
        c = string[i]

        if c not in char_index:
            char_index[c] = []
        
        char_index[c].append(i)

        couple = c_prev + c

        if couple not in couples_index:
            couples_index[couple] = []
        
        couples_index[couple].append(i)
        
        c_prev = c
        i += 1

    
    has_two_letters_pairs = False
    for couple, indexes in couples_index.items():
        if len(indexes) < 2:
            continue

        for i, index in enumerate(indexes[1:], start=1):
            prev_index = indexes[i-1] 
            if  (prev_index + 1) == index:
                continue

            has_two_letters_pairs = True
            break


    has_same_letter_split_by_another = False
    for c, indexes in char_index.items():
        if len(indexes) < 2:
            continue

        for i, index in enumerate(indexes[1:], start=1):
            prev_index = indexes[i-1]
            if (prev_index + 2) == index:
                has_same_letter_split_by_another = True
                break
    
    return has_two_letters_pairs and has_same_letter_split_by_another

# lines = [
#     "qjhvhtzxzqqjkmpb",
#     "xxyxx",
#     "uurcxstgmygtbstg",
#     "ieodomkazucvgmuy",
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

# print(nice_lines)
# print(naughty_lines)


