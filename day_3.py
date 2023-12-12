"""
This adheres a solution of Day 3 puzzle
- https://adventofcode.com/2023/day/3
"""

from os import getcwd
import re

symbols = r'[^\w\.]'  # not alphanumeric and dot

answer = 0  # hold the expected output

input_file = f"{getcwd()}/input.txt"
inputs = (i for i in open(input_file))

for input_line in inputs:
    input_line = input_line.strip()
    print(input_line, end=" --> ")

    print(f"sym-ctrl: {re.findall(symbols, input_line)}")

    # answer += game_id

print(f"[[[ Final Answer Is: {answer} ]]]")
