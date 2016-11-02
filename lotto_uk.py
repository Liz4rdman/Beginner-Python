#!/usr/bin/env python3

# This program selects 6 numbers for your lotto ticket,
# based on the 6 numbers which came out most out of 1 million
# randomly generated numbers

import random
import math
from collections import Counter

print('***************************')
print('Welcome to the Lotto Picker')
print('***************************')
print()


def get_random_number():
    return math.floor(random.random() * 59) + 1

guess = 0
numlist = []

while guess <= 1000000:
    numlist.append(get_random_number())
    guess += 1

x = (Counter(numlist))

print('Out of {} guesses, the top 6 numbers were: '.format(guess - 1), '\n')

for number, amount in x.most_common(6):
    print('Number {} came out {} times'.format(number, amount))
