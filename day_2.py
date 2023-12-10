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
    print(input_line.strip(), end=" --> ")

    game_id, records = input_line.strip().split(": ")
    game_id = int(game_id.replace("Game", "").strip())
    records = re.split("; ", records)
    print(f"[#{game_id}] {records}")

    answer += game_id

print(f"[[[ Final Answer Is: {answer} ]]]")
