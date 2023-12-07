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
    Enumerate through digit_letters and
    replace all of its occurrences in line.
    Return a list of digit characters.
    """

    for i, letters in enumerate(digit_letters):
        line = re.sub(letters, str(i), line)

    return [x for x in list(line) if x.isdigit()]


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
