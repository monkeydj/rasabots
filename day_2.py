"""
This adheres a solution of Day 2 puzzle - https://adventofcode.com/2023/day/2
"""

from os import getcwd
import re

input_file = f"{getcwd()}/input.txt"

LOADED_CUBES = {"red": 12, "green": 13, "blue": 14}

answer = None

with open(input_file) as fd:
    while True:
        input_line = fd.readline()
        if not input_line:
            break

        print(input_line.strip(), end=" --> ")

        game_id, records = input_line.strip().split(": ")
        game_id = int(game_id.replace("Game", "").strip())
        records = re.split("; ", records)
        print(f"[#{game_id}] {records}")

print(f"[[[ Final Answer Is: {answer} ]]]")
