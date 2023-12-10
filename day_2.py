"""
This adheres a solution of Day 2 puzzle - https://adventofcode.com/2023/day/2
"""

from os import getcwd
import re

CUBES_IN_BAG = {"red": 12, "green": 13, "blue": 14}

answer = 0  # hold the expected output

input_file = f"{getcwd()}/input.txt"
inputs = (i for i in open(input_file))


def extract(game_inputs):
    for data in re.split("; ", game_inputs):
        elf_s_hand = re.findall(r'(\d+) (blue|red|green)', data)
        print(f" --> {elf_s_hand}", end=" --> ...")

        for cube in elf_s_hand:
            yield cube


def is_possible(game_inputs):
    for count, cube_color in extract(game_inputs):
        if int(count) > CUBES_IN_BAG.get(cube_color, 0):
            print("ERRORED!!")
            return False
        else:
            print("PASS")

    return True


for input_line in inputs:
    input_line = input_line.strip()
    print(input_line)

    game_id, game_inputs = input_line.split(": ")
    game_id = int(game_id.replace("Game", "").strip())

    if is_possible(game_inputs):
        answer += game_id

print(f"[[[ Final Answer Is: {answer} ]]]")
