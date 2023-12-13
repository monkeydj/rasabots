"""
This adheres a solution of Day 4 puzzle
- https://adventofcode.com/2023/day/4
"""

from sys import argv

scratchcards = open(argv[1]).read().split('\n')

for card in scratchcards:
    print(card)
