#!/usr/bin/python3

from random import random

bot_hand = random()
user_hand = input('Enter a number:')

if float(user_hand) <= bot_hand:
    print('Eh...')
else:
    print('Win somhow!')
