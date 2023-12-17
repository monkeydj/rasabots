"""
This adheres a solution of Day 7 puzzle
- https://adventofcode.com/2023/day/7
"""


def compare(hand_a: str, hand_b: str) -> int:
    return 0


camel_game = open("data.in").read().split("\n")

answer = 0

for a_hand in camel_game:
    cards, bid = a_hand.split()
    print(f"hand: {cards} bid= {bid}")

print(f"[Total Winnings Is: {answer}]")
