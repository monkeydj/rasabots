"""
This adheres a solution of Day 2 puzzle Part Two
- https://adventofcode.com/2023/day/2#part2
"""

from os import getcwd
import re


def count_least_cubes(color: str, game_inputs: str) -> int:
    colored_cubes = re.findall(rf'(\d+) {color}', game_inputs)
    least_count = max(*[int(x) for x in colored_cubes])

    print(f" --> {color}: {colored_cubes} --> {least_count}")

    return least_count


def get_cube_powers(game_inputs: str) -> int:
    return count_least_cubes("red", game_inputs) * \
        count_least_cubes("green", game_inputs) * \
        count_least_cubes("blue", game_inputs)


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
