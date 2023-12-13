"""
This adheres a solution of Day 3 puzzle Part Two
- https://adventofcode.com/2023/day/3#part2

"""

from collections import defaultdict
from sys import argv

import re


def get_surrounding_indexes(r_i: int, start: int, end: int) -> list[tuple]:
    rows = [r_i + r for r in [-1, 0, 1]]
    cols = range(start - 1, end + 1)
    surrounding = [(x, y) for x in rows for y in cols]

    return surrounding


# --- main process ----

engine_schematic = open(argv[1]).read().split()
found_gear_parts = defaultdict(list)

answer = 0

for cr, engine_line in enumerate(engine_schematic):
    for number in re.finditer(r'\d+', engine_line):
        surrounding = get_surrounding_indexes(cr, number.start(), number.end())

        print(number, surrounding)

        for x, y in surrounding:
            if any([not (0 <= x < len(engine_schematic)),
                   not (0 <= y < len(engine_schematic[cr]))]):
                continue

            if engine_schematic[x][y] != '*':
                continue

            found_gear_parts[(x, y)].append((cr, number))

            print((x, y, found_gear_parts[(x, y)]))

            if len(found_gear_parts[(x, y)]) == 2:
                part_numbers = [int(number.group(0))
                                for cr, number in found_gear_parts[(x, y)]]
                answer += part_numbers[0] * part_numbers[1]

print(f"[ Total Gear Ratio Is: {answer} ]")
