"""
This adheres a solution of Day 3 puzzle
- https://adventofcode.com/2023/day/3
"""

from os import getcwd

import re


def mark(part_number: re.Match, output_line: str = "") -> str:
    # ref: https://stackoverflow.com/a/51708889/8546076
    marked = "\033[4m\033[92m" + part_number.group(0) + "\033[0m"
    first_half = output_line[:part_number.start()]
    second_half = output_line[part_number.end():]

    return first_half + marked + second_half


def check_part_number(number: re.Match, engine_line: str) -> bool:
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

    return connected is not None


# --- main process ----

input_file = f"{getcwd()}/input.txt"
inputs = (i for i in open(input_file))

answer = 0  # hold the expected output

prev_line, obscure_numbers = None, []
output_line = None

for input_line in inputs:
    parts_sum, engine_line = 0, input_line.strip()

    while len(obscure_numbers) > 0:
        number, obscure_numbers = obscure_numbers[0], obscure_numbers[1:]

        if check_part_number(number, engine_line):
            parts_sum += int(number.group(0))
            output_line = mark(number, output_line)

    if output_line:
        print(output_line)
    # * this marks the end of processing one input_line

    output_line = engine_line

    for number in re.finditer(r'\d+', engine_line):
        is_part_number = check_part_number(number, engine_line)
        is_part_number |= check_part_number(number, prev_line)

        if is_part_number:
            parts_sum += int(number.group(0))
            output_line = mark(number, output_line)
        else:
            # ! only track number if not yet found connected
            obscure_numbers.append(number)

    prev_line = engine_line  # track for next iteration
    answer += parts_sum

print(output_line)  # very last line

print(f"[[[ Final Answer Is: {answer} ]]]")
