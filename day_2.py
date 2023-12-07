"""
This adheres a solution of Day 2 puzzle - https://adventofcode.com/2023/day/2
"""

from os import getcwd

input_file = f"{getcwd()}/input.txt"
answer = None

with open(input_file) as fd:
    while True:
        input_line = fd.readline()
        if not input_line:
            break

        print(input_line.strip())

print(f"[[[ Final Answer Is: {answer} ]]]")
