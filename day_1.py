"""
This adheres a solution of day 1 puzzle
https://adventofcode.com/2023/day/1
"""

from os import getcwd

input_file = f"{getcwd()}/input.txt"

with open(input_file) as fd:
    while True:
        input_line = fd.readline()
        if not input_line:
            break

        print(input_line.strip())
