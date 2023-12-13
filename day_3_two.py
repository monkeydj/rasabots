"""
This adheres a solution of Day 3 puzzle Part Two
- https://adventofcode.com/2023/day/3#part2

"""

from collections import defaultdict
from sys import argv


def calculate_gear_ratio(engine_schematic):
    # NOTE: Bard helped me - https://g.co/bard/share/3cd2369c7b9e
    gears = []
    for i in range(len(engine_schematic)):
        for j in range(len(engine_schematic[i])):
            if engine_schematic[i][j] == "*":
                # Check if the symbol is adjacent to two digits
                if (
                    0 <= i - 1 < len(engine_schematic)
                    and 0 <= j - 1 < len(engine_schematic[i])
                    and engine_schematic[i - 1][j - 1].isdigit()
                    and 0 <= i + 1 < len(engine_schematic)
                    and 0 <= j + 1 < len(engine_schematic[i])
                    and engine_schematic[i + 1][j + 1].isdigit()
                ):
                    # Add the gear to the list with its gear ratio
                    gears.append(
                        (
                            int(engine_schematic[i - 1][j - 1]),
                            int(engine_schematic[i + 1][j + 1]),
                        )
                    )


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


def get_area_indexes(r_i: int, start: int, end: int) -> list[tuple]:
    rows, cols = [r_i + r for r in [-1, 0, 1]], range(start, end + 1)
    return [(x, y) for x in rows for y in cols]


# --- main process ----
engine_schematic = open(argv[1]).read().split()
found_gear_parts = defaultdict(list)

for cr, engine_line in enumerate(engine_schematic):
    for number in re.finditer(r'\d+', engine_line):
        area = get_area_indexes(cr, number.start(), number.end())

        for x, y in area:
            if any([not (0 <= x < len(engine_schematic)),
                   not (0 <= y < len(engine_schematic[cr]))]):
                continue

            if engine_schematic[x][y] == '*':
                print(number)


# mark(found_part_numbers, prev_line)  # very last line

answer = 0  # //TODO: calculate the final answer here
print(f"[ Total Gear Ratio Is: {answer} ]")
