"""
This adheres a solution of day 1 puzzle *Part Two*
https://adventofcode.com/2023/day/1
"""

from os import getcwd
import re

input_file = f"{getcwd()}/input.txt"
answer = 0

digit_letters = (
    "zero", "one", "two", "three", "four",
    "five", "six", "seven", "eight", "nine"
)


def find_digits(line: str = "") -> list[str]:
    """
    Enumerate through every letter in line, check if it's a digit, 
    or create a combination of 3-5 letters & compare against digit_letters.
    Return a list of found digit characters.
    """
    digits, combi = [], ""
    while len(line) > 0:
        x, line = line[0], line[1:]
        print(f"[debug] x={x} combi={combi}")
        if x.isdigit():
            digits.append(x)
            combi = ""  # reset combination
        else:
            combi += x
            if combi in digit_letters:
                digits.append(str(digit_letters.index(combi)))  # quite ugly
                combi = ""  # reset as found

    return digits


with open(input_file) as fd:
    while True:
        input_line = fd.readline()
        if not input_line:
            break

        print(input_line.strip(), end=" ---> ")

        digits = find_digits(input_line.strip())

        print(list(digits), end=" ---> ")

        number = int(digits[0] + digits[-1]) if len(digits) > 0 else 0

        print(number)

        answer += number

print(f"[[[ Final Answer Is, {answer} ]]]")
