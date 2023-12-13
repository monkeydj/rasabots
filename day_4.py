"""
This adheres a solution of Day 4 puzzle
- https://adventofcode.com/2023/day/4
"""

from sys import argv

import re

scratchcards = open(argv[1]).read().split('\n')

answer = 0

for card in scratchcards:
    print(card, end=" --> ")

    winning, having = re.sub(r"Card \d+: ", "", card).split(" | ")
    winning, having = winning.split(), having.split()
    print(winning, "x", having, end=" = ")

    scored = 0
    for n in having:
        if n in winning:
            scored = 1 if scored == 0 else scored * 2

    print(scored)

    answer += scored

print(f"[Total Score Is: {answer}]")
