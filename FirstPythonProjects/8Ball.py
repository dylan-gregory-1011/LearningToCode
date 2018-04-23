#!/usr/bin/env python
"""
A sorry excuse for a game that replicates the fun of an 8 Ball.  Ask the
magical python 8ball a question and you will be answered with the best confidence
that a random number generator can execute.
"""

import random
import time

__author__ = "Dylan Smith"
__copyright__ = "Copyright (C) 2016 Dylan Smith"
__credits__ = ["Dylan Smith"]

__license__ = "Public Domain"
__version__ = "1.0"
__maintainer__ = "Dylan Smith"
__email__ = "-"
__status__ = "Development"

playing = 'Y'

#question = raw_input('What is your question?')


answers = ['likely', 'like there is no chance', 'doubtful', 'probable', 'cloudy']
def question():
    question = raw_input('What would you like to know?\n')
    #print question
    magic = random.randint(0,4)
    time.sleep(2)
    response = answers[magic]
    print 'The outcome looks %s' %(response)
    end()

def end():
    print 'Do you want to play again?'
    Replay = raw_input("Do you want to play again? Yes or No ")
    if Replay != 'No':
        question()
    else:
        print 'Thanks for playing!!!'

question()
