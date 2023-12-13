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
    winning, having = winning.split(), having.split()

    # (Cards will never make you copy a card past the end of the table.)
    scored = 0
    for n in having:
        if n in winning:
            scored = 1 if scored == 0 else scored * 2
            winnng_copies[i + (scored // 2)] += 1

    print(scored, "copies=", winnng_copies[i])

answer = sum(winnng_copies)
print(f"[Total Score Is: {answer}]")
