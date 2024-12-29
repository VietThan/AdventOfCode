"""
--- Part Two ---
Now find one that starts with six zeroes.
"""

import hashlib

prefix = "iwrupvqb"

found = False

num = 1

while (not found):
    input = prefix + str(num)
    out_hash = hashlib.md5(input.encode("utf-8"))
    out_hex = out_hash.hexdigest()

    if out_hex[:6] == "000000":
        found = True
        print(f"Found {input = } has {out_hex = }")
        break

    num += 1