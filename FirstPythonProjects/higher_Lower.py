"""
Can you guess the actual number
"""

import random

def guessing_Game():
    num = random.randint(0,100)
    guess = input("What is your first guess?")

    while guess != num:
        if(guess>num):
            print "Your guess is too high"
            guess = input("What is your new guess")
            continue
        elif(guess<num):
            print "Your guess is too low"
            guess = input("What is your new guess")
            continue

    print "Your guess of %i is the same as our calculated number %i" %(guess, num)

guessing_Game()
