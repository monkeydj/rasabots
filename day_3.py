"""
This adheres a solution of Day 3 puzzle
- https://adventofcode.com/2023/day/3
"""

from os import getcwd

import re


def mark(part_numbers: list[re.Match], output_line: str = ""):
    """
    Print out found part_numbers highlighted in output_line.
    """
    chunk_start = 0
    # as they are found not in order of appearance in output_line
    part_numbers_ordered = sorted(part_numbers, key=lambda n: n.start())

    for number in part_numbers_ordered:
        print(output_line[chunk_start:number.start()], end="")
        # ref: https://stackoverflow.com/a/51708889/8546076
        print("\033[4m\033[92m" + number.group(0) + "\033[0m", end="")

        chunk_start = number.end()

    print(output_line[chunk_start:])  # whatever left


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

prev_line, obscure_numbers, found_part_numbers = None, [], []

for input_line in inputs:
    parts_sum, engine_line = 0, input_line.strip()

    while len(obscure_numbers) > 0:
        number, obscure_numbers = obscure_numbers[0], obscure_numbers[1:]

        if check_part_number(number, engine_line):
            parts_sum += int(number.group(0))
            found_part_numbers.append(number)

    if prev_line:
        mark(found_part_numbers, prev_line)
        found_part_numbers = []  # reset
    # * this marks the end of processing one input_line

    for number in re.finditer(r'\d+', engine_line):
        is_part_number = check_part_number(number, engine_line)
        is_part_number |= check_part_number(number, prev_line)

        if is_part_number:
            parts_sum += int(number.group(0))
            found_part_numbers.append(number)
        else:
            # ! only track number if not yet found connected
            obscure_numbers.append(number)

    prev_line = engine_line  # track for next iteration
    answer += parts_sum

mark(found_part_numbers, prev_line)  # very last line

print(f"[[[ Final Answer Is: {answer} ]]]")
