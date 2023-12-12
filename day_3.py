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


def check_part_number(number: re.Match, engine_line: str) -> int | None:
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

    return int(number.group(0)) if connected else None


for engine_line in inputs:
    parts_sum, engine_line = 0, engine_line.strip()

    while len(prev_numbers) > 0:
        number, prev_numbers = prev_numbers[0], prev_numbers[1:]
        part_number = check_part_number(number, engine_line)

        if part_number:
            parts_sum += part_number
            print(part_number, end="/")

    print("\n", engine_line, end=" -> ")

    for number in re.finditer(r'\d+', engine_line):
        part_number = check_part_number(number, prev_line) or \
            check_part_number(number, engine_line)

        if not part_number:
            # ! only track number if not yet found connected
            prev_numbers.append(number)
        else:
            parts_sum += part_number
            print(part_number, end="/")

    prev_line = engine_line  # track for next iteration
    answer += parts_sum

print(f"\n[[[ Final Answer Is: {answer} ]]]")
