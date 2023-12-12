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
prev_line = None
prev_numbers = []


def check_part_number(number: re.Match, engine_line: str) -> int:
    """
    As one may be adjacent to one or many symbols, so simply
    find if any symbol is around number's span in engine_line.
    """
    if engine_line is None or len(engine_line) == 0:
        return 0

    start = number.start() - 1 if number.start() > 0 else 0
    end = number.end() + 1 if number.end() < len(engine_line) else 0
    engine_slice = engine_line[start: end]
    connected = re.search(r'[^\w\.]', engine_slice)

    return int(number.group(0)) if connected else 0


for engine_line in inputs:
    engine_line = engine_line.strip()
    print(engine_line, end=" ---> ")

    parts_sum = 0

    while len(prev_numbers) > 0:
        number, prev_numbers = prev_numbers[0], prev_numbers[1:]
        parts_sum += check_part_number(number, engine_line)
        print(parts_sum, end="/")

    for number in re.finditer(r'\d+', engine_line):
        prev_numbers.append(number)  # track found number
        parts_sum += check_part_number(number, prev_line)
        parts_sum += check_part_number(number, engine_line)
        print(parts_sum, end="/")

    answer += parts_sum

    prev_line = engine_line
    print()  # end of line


print(f"[[[ Final Answer Is: {answer} ]]]")
