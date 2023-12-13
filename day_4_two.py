"""
This adheres a solution of Day 4 puzzle Part Two
- https://adventofcode.com/2023/day/4#part2
"""

from sys import argv

import re

scratchcards = open(argv[1]).read().split('\n')
having_copies = [1] * len(scratchcards)  # even not yet won

for i, card in enumerate(scratchcards):

    card_no, winning, having = re.split(r"\s?[:|] ", card)
    matched = [n for n in having.split() if n in winning.split()]

    print(card_no + ":", matched, end=" = ")

    scored = 0 if len(matched) == 0 else 2 ** (len(matched) - 1)

    # win that many copies of next card
    for n in range(len(matched)):
        # (Cards will never make you copy a card past the end of the table.)
        having_copies[i + n + 1] += having_copies[i]

    print("scored=", scored, "copies=", having_copies[i])

answer = sum(having_copies)
print(f"[Total Score Is: {answer}]")
