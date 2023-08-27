#!/usr/bin/python3

import time
from sys import argv
from random import randrange

if len(argv) == 2:
    user_hand = float(argv[1])
    print(f"Got a number: [{user_hand}]")
else:
    user_hand = float(input("Enter a number: "))

print("and Bot hand is...", end=" ")

time.sleep(randrange(0, 3))
bot_hand = randrange(0, user_hand * 2)

print(f"[{bot_hand}]")

if float(user_hand) <= bot_hand:
    print("Eh...")
else:
    print("!!! You Win Luckily !!!")

if __name__ == "__main__":
    pass
