"""
This adheres a solution of Day 4 puzzle Part Two
- https://adventofcode.com/2023/day/4#part2
"""

from sys import argv

import re

scratchcards = open(argv[1]).read().split('\n')
winnng_copies = [0] * len(scratchcards)

for i, card in enumerate(scratchcards):
    print(card, end=" --> ")

    winning, having = re.sub(r"Card \d+: ", "", card).split(" | ")
    matched = [n for n in having.split() if n in winning.split()]

    print(matched, end=" = ")

    scored = 0 if len(matched) == 0 else 2 ** (len(matched) - 1)
    if scored > 0:
        # win a copy of itself first
        winnng_copies[i] += 1
    # then, win a copy of next card
    for n in range(len(matched)):
        # (Cards will never make you copy a card past the end of the table.)
        winnng_copies[i + n + 1] += 1

    print(scored, "copies=", winnng_copies[i])

answer = sum(winnng_copies)
print(f"[Total Score Is: {answer}]")
