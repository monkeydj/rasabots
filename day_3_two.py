"""
This adheres a solution of Day 3 puzzle Part Two
- https://adventofcode.com/2023/day/3#part2

"""

from collections import defaultdict
from sys import argv

import re


def index_surrounding(r_i: int, start: int, end: int) -> list[tuple]:
    rows = [r_i + r for r in [-1, 0, 1]]
    cols = range(start - 1, end + 1)
    surrounding = [(x, y) for x in rows for y in cols]

    return surrounding


# --- main process ----

engine_schematic = open(argv[1]).read().split()
found_gear_parts = defaultdict(list)

for cr, engine_line in enumerate(engine_schematic):
    for number in re.finditer(r'\d+', engine_line):
        surrounding = index_surrounding(cr, number.start(), number.end())

        print(number, surrounding)

        for x, y in surrounding:
            if any([not (0 <= x < len(engine_schematic)),
                   not (0 <= y < len(engine_schematic[cr]))]):
                continue

            if engine_schematic[x][y] != '*':
                continue

            found_gear_parts[(x, y)].append(int(number.group(0)))
            print((x, y, found_gear_parts[(x, y)]))  # after addition


answer = sum([part_numbers[0] * part_numbers[1]
              for part_numbers in found_gear_parts.values()
              if len(part_numbers) == 2])

print(f"[ Total Gear Ratio Is: {answer} ]")
