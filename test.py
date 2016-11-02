#!/usr/bin/env python3

# Let the computer choose your 6 Lotto(UK) numbers (between 1-59)
# based on 1 million random guesses.


import random
import math
from collections import Counter

print('***************************')
print('Welcome to the Lotto Picker')
print('***************************')
print()
guess = 0
numlist = []

def getRandomNumber():
    while guess <=1000000:
        return math.floor(random.random() * 59) + 1


    randomNumber = getRandomNumber()

    numlist.append(randomNumber)
    guess += 1
    numlist.append(randomNumber)

x = (Counter(numlist))

print('Out of {} guesses, the top 6 numbers were: '.format(guess - 1), '\n')

for number, amount in x.most_common(6):
    print('Number {}, which came out {} times'.format(number, amount))
