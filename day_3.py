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

    engine_slice = engine_line[number.start() - 1:number.end() + 1]
    connected = re.search(r'[^\w\.]', engine_slice)

    return int(number.group(0)) if connected else 0


def unwind_schemetic(engine_line: str) -> int:
    """
    Try to unwind each line & prev. tracked line of the engine schemetic.
    """
    parts_sum = 0

    for number in re.finditer(r'\d+', engine_line):
        prev_numbers.append(number)  # track found number
        parts_sum += check_part_number(number, prev_line)
        parts_sum += check_part_number(number, engine_line)

    return parts_sum


for input_line in inputs:
    input_line = input_line.strip()
    print(input_line, end=" ---> ")

    parts_sum = 0

    while len(prev_numbers) > 0:
        number, prev_numbers = prev_numbers[0], prev_numbers[1:]
        parts_sum += check_part_number(number, input_line)
        print(parts_sum, end="/")

    parts_sum += unwind_schemetic(input_line)
    print(parts_sum)

    answer += parts_sum

    prev_line = input_line


print(f"[[[ Final Answer Is: {answer} ]]]")