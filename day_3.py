"""
This adheres a solution of Day 3 puzzle
- https://adventofcode.com/2023/day/3
"""

from os import getcwd

import re


input_file = f"{getcwd()}/input.txt"
inputs = (i for i in open(input_file))

answer = 0  # hold the expected output

# TODO: make a closure to not have this var 'globally'
prev_input = None
prev_symbols = []


def find_part_numbers(input_line: str) -> int:
    symbols, part_numbers = r'[^\w\.]', []

    for sym in re.finditer(symbols, input_line):
        span = sym.span()
        prev_symbols.append(span)  # track found symbols

        if prev_input is not None:
            prev_slice = prev_input[span[0] - 3:span[1] + 3]
            part_numbers += re.findall(r'\d+', prev_slice)

        # find numbers before or after symbols (not dot)
        input_slice = input_line[span[0] - 3:span[1] + 3]
        part_numbers += re.findall(r'\d+', input_slice)

    return sum([int(x) for x in part_numbers])


for input_line in inputs:
    input_line = input_line.strip()
    print(input_line, end=" ---> ")

    parts_sum = 0

    while len(prev_symbols) > 0:
        prev_span, prev_symbols = prev_symbols[0], prev_symbols[1:]
        input_slice = input_line[prev_span[0] - 3:prev_span[1] + 3]
        new_part_numbers = re.findall(r'\d+', input_slice)
        parts_sum += sum([int(x) for x in new_part_numbers])
        print(parts_sum, end=" + ")

    parts_sum += find_part_numbers(input_line)
    print(parts_sum)

    answer += parts_sum

    prev_input = input_line  # track previously loaded


print(f"[[[ Final Answer Is: {answer} ]]]")
