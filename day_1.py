"""
This adheres a solution of day 1 puzzle
https://adventofcode.com/2023/day/1
"""

from os import getcwd

input_file = f"{getcwd()}/input.txt"
answer = 0

with open(input_file) as fd:
    while True:
        input_line = fd.readline()
        if not input_line:
            break

        print(input_line.strip(), end=" ---> ")

        chars = list(input_line.strip())
        digits = [x for x in chars if x.isdigit()]

        print(list(digits), end=" ---> ")

        number = int(digits[0] + digits[-1]) if len(digits) > 0 else 0

        print(number)

        answer += number

print(f"[[[ Final Answer Is: {answer} ]]]")
