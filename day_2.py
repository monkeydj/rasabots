"""
This adheres a solution of Day 2 puzzle - https://adventofcode.com/2023/day/2
"""

from os import getcwd
import re

LOADED_CUBES = {"red": 12, "green": 13, "blue": 14}

answer = 0  # hold the expected output

input_file = f"{getcwd()}/input.txt"
inputs = (i for i in open(input_file))

for input_line in inputs:
    input_line = input_line.strip()
    print(input_line)

    game_id, records = input_line.split(": ")
    game_id = int(game_id.replace("Game", "").strip())

    for rec in re.split("; ", records):
        print(f" --> [#{game_id}] {rec}", end=" --> ...\n")

    answer += game_id

print(f"[[[ Final Answer Is: {answer} ]]]")
