#!/usr/bin/python3

import time
from random import randrange

user_hand = float(input('Enter a number: '))

print("and Bot hand is... ", end=" ")

time.sleep(randrange(0, 3))
bot_hand = randrange(0, user_hand * 2)

print(f'**{bot_hand}**')

if float(user_hand) <= bot_hand:
    print('Eh...')
else:
    print('Win somehow!!!')
