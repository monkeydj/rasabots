"""
This adheres a solution of Day 4 puzzle Part Two
- https://adventofcode.com/2023/day/4#part2
"""

from sys import argv

import re

scratchcards = open(argv[1]).read().split('\n')
winnng_copies = [0] * len(scratchcards)

answer = 0

for n, card in enumerate(scratchcards):
    print(card, end=" --> ")

    winning, having = re.sub(r"Card \d+: ", "", card).split(" | ")
    winning, having = winning.split(), having.split()
    # print(winning, "x", having, end=" = ")
    # (Cards will never make you copy a card past the end of the table.)
    copies = 0
    for n in having:
        if n in winning:
            copies += 1

    print(copies)

    answer += copies

print(f"[Total Score Is: {answer}]")
