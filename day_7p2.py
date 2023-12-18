"""
This adheres a solution of Day 7 puzzle
- https://adventofcode.com/2023/day/7
"""

from collections import Counter

JOKER = 'J'
CARDS = [JOKER] + list(reversed('AKQJT98765432'))


def get_counter(cards: str) -> Counter:
    counter = Counter(cards)
    jokers = counter.pop(JOKER, 0)

    if not counter:  # only exception when all cards are J
        return {JOKER: jokers}

    c_most = max(counter, key=counter.get)
    # assume jokers to be cards with highest count
    counter[c_most] += jokers

    return counter


def get_kind(cards: str) -> int:
    c_cnt = sorted(get_counter(cards).values())

    if c_cnt == [5]:  # five of a kind
        return 5
    elif c_cnt == [1, 4]:  # four of a kind
        return 4
    elif c_cnt == [2, 3]:  # three of a kind + a pair
        return 3.5
    elif c_cnt == [1, 1, 3]:  # three of a kind
        return 3
    elif c_cnt == [1, 2, 2]:  # 2 pairs
        return 2.5
    elif c_cnt == [1, 1, 1, 2]:  # a pair
        return 2

    return 0  # any high card


def check_hand(hand: str) -> set:
    cards, _ = hand.split()
    strengths = [CARDS.index(c) for c in cards]
    return [get_kind(cards), *strengths]


camel_game = open("data.in").read().split("\n")
ranked_game = enumerate(sorted(camel_game, key=check_hand))

answer = 0

for rank, a_hand in ranked_game:
    cards, bid = a_hand.split()
    print(f"hand: {cards} bid= {bid}")

    answer += int(bid) * (rank + 1)

print(f"[Total Winnings Is: {answer}]")
