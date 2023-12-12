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


def check_part_numbers(input_line: str, symbols: str = r'[^\w\.]') -> int:
    # not alphanumeric and dot
    print(f" --> sym-ctrl: {re.findall(symbols, input_line)}")

    # search numbers before or after symbols (not dot)
    search = rf'(\d+(?={symbols})|(?<={symbols})\d+)'
    part_numbers = re.findall(search, input_line)
    print(f" --> parts: {part_numbers}")

    return sum([int(x) for x in part_numbers])


for input_line in inputs:
    input_line = input_line.strip()
    print(input_line)

    answer += check_part_numbers(input_line)

    prev_input = input_line  # track previously loaded input

print(f"[[[ Final Answer Is: {answer} ]]]")
