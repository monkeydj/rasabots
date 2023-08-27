#!/usr/bin/python3

import time
from sys import argv
from random import randrange


def getUserHand():

    if len(argv) == 2:
        user_hand = float(argv[1])
        print(f"Got a User hand: [{user_hand}]")
    else:
        user_inputs = input("Enter a number for your hand: ")
        user_hand = float(user_inputs)

    return user_hand


def getBotHand(user_hand=10):

    print("and Bot hand is...", end=" ")

    time.sleep(randrange(0, 3))
    bot_hand = randrange(0, user_hand * 2)

    print(f"[{bot_hand}]")

    return bot_hand


def start():

    user_hand = getUserHand()
    bot_hand = getBotHand(user_hand)  # cheat purposefully

    if float(user_hand) <= bot_hand:
        print("Eh...")
    else:
        print("!!! You Win Luckily !!!")


if __name__ == "__main__":
    start()
