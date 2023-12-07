"""
This adheres a solution of day 1 puzzle *Part Two*
https://adventofcode.com/2023/day/1
"""

from os import getcwd, getenv
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=getenv("LOG_LEVEL", "INFO").upper())

input_file = f"{getcwd()}/input.txt"
answer = 0

digit_letters = (
    "zero", "one", "two", "three", "four",
    "five", "six", "seven", "eight", "nine"
)


def get_spelled_digit(letters: str = "") -> str | None:
    logger.debug(f"letters={letters}")
    return letters if letters.isdigit() \
        else str(digit_letters.index(letters)) if letters in digit_letters \
        else None


def find_digits(line: str = "") -> list[int]:
    """
    Enumerate through every letter in line, check if it's a digit,
    or create a combination of 3-5 letters & compare against digit_letters.
    Return a list of found digit characters.

    NOTE: it still consider consecutive digits also as one digit.
    eg. '241' is [2, 241, 4, (41, )? 1]
    """
    logger.debug(f"line={line}")

    if len(line) == 0:
        return []

    digits = [get_spelled_digit(line[0])]

    if len(line) >= 3:  # check one, two, six
        digits.append(get_spelled_digit(line[:3]))
    if len(line) >= 4:  # check four, five, nine
        # * zero can be found here, but the puzzle didn't include it
        digits.append(get_spelled_digit(line[:4]))
    if len(line) >= 5:  # check three, seven, eight
        digits.append(get_spelled_digit(line[:5]))

    digits += find_digits(line[1:])

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
