"""
This adheres a solution of Day 3 puzzle Part Two
- https://adventofcode.com/2023/day/3#part2

"""

from os import getcwd


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

    total_gear_ratio = sum(a * b for a, b in gears)
    return total_gear_ratio


# --- main process ----

engine_schematic = open(f"{getcwd()}/input.txt").read().split()
total_gear_ratio = calculate_gear_ratio(engine_schematic)
print(f"Total gear ratio: {total_gear_ratio}")
