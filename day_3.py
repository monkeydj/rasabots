"""
This adheres a solution of Day 3 puzzle
- https://adventofcode.com/2023/day/3
"""

from functools import reduce
from os import getcwd

import re

input_file = f"{getcwd()}/input.txt"
inputs = (i for i in open(input_file))

answer = 0  # hold the expected output

# TODO: make a closure to not have this var 'globally'
prev_input = None


def find_part_numbers(input_line: str) -> int:
    symbols, part_numbers = r'[^\w\.]', []

    for sym in re.finditer(symbols, input_line):
        span = sym.span()

        print(f" --> symbol [{sym.group(0)}, span={span}]")

        # find numbers before or after symbols (not dot)
        part_numbers += re.findall(r'\d+', input_line[span[0] - 3:span[0]])
        part_numbers += re.findall(r'\d+', input_line[span[1]:span[1] + 3])

        if prev_input is not None:
            schemetic_slice = prev_input[span[0] - 3:span[1] + 3]
            part_numbers += re.findall(r'\d+', schemetic_slice)

    print(f" --> parts: {part_numbers}")

    return sum([int(x) for x in part_numbers])


for input_line in inputs:
    input_line = input_line.strip()
    print(input_line)

    answer += find_part_numbers(input_line)

    prev_input = input_line  # track previously loaded input

print(f"[[[ Final Answer Is: {answer} ]]]")
