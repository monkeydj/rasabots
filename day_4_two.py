"""
This adheres a solution of Day 4 puzzle Part Two
- https://adventofcode.com/2023/day/4#part2
"""

from sys import argv

import re

scratchcards = open(argv[1]).read().split('\n')
winnng_copies = [0] * len(scratchcards)

for i, card in enumerate(scratchcards):

    card_no, winning, having = re.split(r"\s?[:|] ", card)
    matched = [n for n in having.split() if n in winning.split()]

    print(card_no + ":", matched, end=" = ")

    scored = 0 if len(matched) == 0 else 2 ** (len(matched) - 1)
    if scored > 0:
        # win a copy of itself first
        winnng_copies[i] += 1
    # then, win that many copies of next card
    for n in range(len(matched)):
        # (Cards will never make you copy a card past the end of the table.)
        winnng_copies[i + n + 1] += winnng_copies[i]

    print("scored=", scored, "copies=", winnng_copies[i])

answer = sum(winnng_copies)
print(f"[Total Score Is: {answer}]")
