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


def find_part_numbers(span: [int, int], engine_line: str) -> int:
    """
    Find numbers around a symbol span.
    """
    engine_slice = engine_line[span[0] - 3:span[1] + 3]
    engine_numbers = re.findall(r'\d+', engine_slice)

    return sum([int(x) for x in engine_numbers])


def unwind_schemetic(engine_line: str) -> int:
    """
    Try to unwind each line & prev. tracked line of the engine schemetic:
    """
    symbols, parts_sum = r'[^\w\.]', 0

    for sym in re.finditer(symbols, engine_line):
        span = sym.span()
        prev_symbols.append(span)  # track found symbols

        if prev_input is not None:
            parts_sum += find_part_numbers(span, prev_input)

        parts_sum += find_part_numbers(span, engine_line)

    return parts_sum


for input_line in inputs:
    input_line = input_line.strip()
    print(input_line, end=" ---> ")

    parts_sum = 0

    while len(prev_symbols) > 0:
        prev_span, prev_symbols = prev_symbols[0], prev_symbols[1:]
        parts_sum += find_part_numbers(prev_span, input_line)
        print(parts_sum, end=" + ")

    parts_sum += unwind_schemetic(input_line)
    print(parts_sum)

    answer += parts_sum

    prev_input = input_line  # track previously loaded


print(f"[[[ Final Answer Is: {answer} ]]]")
