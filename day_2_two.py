"""
This adheres a solution of Day 2 puzzle - https://adventofcode.com/2023/day/2
"""

from os import getcwd
import re

CUBES_IN_BAG = {"red": 12, "green": 13, "blue": 14}

answer = 0  # hold the expected output

input_file = f"{getcwd()}/input.txt"
inputs = (i for i in open(input_file))


def get_powers(game_inputs):
    colored_cubes = re.findall(r'(\d+) (blue|red|green)', game_inputs)

    for count, cube_color in colored_cubes:
        print(f" --> {cube_color}: {count}", end=" --> ...")

        if int(count) > CUBES_IN_BAG.get(cube_color, 0):
            print("ERRORED!!")
            return 0

        print("PASS")

    return 1


for input_line in inputs:
    input_line = input_line.strip()
    print(input_line)

    game_id, game_inputs = input_line.split(": ")
    game_id = int(game_id.replace("Game", "").strip())

    answer += get_powers(game_inputs)

print(f"[[[ Final Answer Is: {answer} ]]]")
