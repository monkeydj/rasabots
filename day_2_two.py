"""
This adheres a solution of Day 2 puzzle Part Two
- https://adventofcode.com/2023/day/2#part2
"""

from os import getcwd
import re


def get_cube_powers(game_inputs):
    colored_cubes = re.findall(r'(\d+) (blue|red|green)', game_inputs)
    cubes_posibility = {"red": 0, "green": 0, "blue": 0}

    for count, cube_color in colored_cubes:
        print(f" --> {cube_color}: {count}", end=" --> ...")
        # TODO: update max value in cubes_posibility

    return cubes_posibility.get("red") * \
        cubes_posibility.get("green") * \
        cubes_posibility.get("blue")


answer = 0  # hold the expected output

input_file = f"{getcwd()}/input.txt"
inputs = (i for i in open(input_file))


for input_line in inputs:
    input_line = input_line.strip()
    print(input_line)

    game_id, game_inputs = input_line.split(": ")
    game_id = int(game_id.replace("Game", "").strip())

    answer += get_cube_powers(game_inputs)

print(f"[[[ Final Answer Is: {answer} ]]]")
