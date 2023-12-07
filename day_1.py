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

        number = digits[0] if len(digits) > 0 else "0"
        number += digits[-1] if len(digits) > 1 else ""

        print(int(number))

        answer += int(number)

print("Final Answer is:", answer)
