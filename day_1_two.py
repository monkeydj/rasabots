"""
This adheres a solution of day 1 puzzle *Part Two*
https://adventofcode.com/2023/day/1
"""

from os import getcwd, getenv
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=getenv("LOG_LEVEL", "DEBUG").upper())

input_file = f"{getcwd()}/input.txt"
answer = 0

digit_letters = (
    "zero", "one", "two", "three", "four",
    "five", "six", "seven", "eight", "nine"
)


def get_spelled_digit(letters: str = "") -> str | None:
    return letters if letters.isdigit() \
        else str(digit_letters.index(letters)) if letters in digit_letters \
        else None


def find_digits(line: str = "") -> list[int]:
    """
    Enumerate through every letter in line, check if it's a digit,
    or create a combination of 3-5 letters & compare against digit_letters.
    Return a list of found digit characters.
    """
    logger.debug(f"line={line}")

    if len(line) == 0:
        return []

    digits = [get_spelled_digit(line)] if len(line) <= 5 else \
        [get_spelled_digit(line[0]), get_spelled_digit(line[:3])] + \
        [get_spelled_digit(line[:4]), get_spelled_digit(line[:5])] + \
        find_digits(line[1:])

    return list(filter(None.__ne__, digits))


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
