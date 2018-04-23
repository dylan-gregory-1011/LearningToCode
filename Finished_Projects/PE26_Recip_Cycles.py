#!/usr/bin/env python
"""finished on completed on 3/7/2018: check all values of d from 1->1000 and update
the max term and value when a longer repeating fraction is found

func getRepeatingCycleFromFraction(Fraction) -> str : this function iterates over the starting index of
the fraction and tries to find a repating term this is because the repeating term doesn't always
start on the first decimal

func checkForIteratingSequence(array) ->str: Check the array that is given for a repeating fraction.
 Slowly add numbers to the repeating term and check the array

"""
from decimal import *
from fractions import Fraction
from math import sqrt,pow
getcontext().prec = 3000

__author__ = "Dylan Smith"
__copyright__ = "Copyright (C) 2018 Dylan Smith"
__credits__ = ["Dylan Smith"]

__license__ = "Public Domain"
__version__ = "1.0"
__maintainer__ = "Dylan Smith"
__email__ = "-"
__status__ = "Development"

def getRepeatingCycleFromFraction(fraction):
    strOfDecimal = str(fraction)
    for initIX in xrange(2,10):
        repeatingCycle = checkForIteratingSequence(strOfDecimal[initIX:])
        if len(repeatingCycle) > 0:
            return repeatingCycle
    return ''

def checkForIteratingSequence(fractionality):
    incrementing_index, repeating_sequence_found = 2, False
    while repeating_sequence_found == False and incrementing_index < len(fractionality)/2:
        repeating_sequence = fractionality[0:incrementing_index]
        if len(set(repeating_sequence)) == 1:
            if incrementing_index == 10:
                return repeatingSequence[0]
        else:
            repeating_sequence_found = True
            for factor_increment in xrange(1,3):
                offset_factor = incrementing_index*factor_increment
                if repeating_sequence == fractionality[offset_factor:offset_factor+len(repeating_sequence)]:
                     continue
                else:
                    repeating_sequence_found = False
                    break
            if repeating_sequence_found == True:
                return repeatingSequence
        incrementing_index+=1
    return ''

if __name__ == '__main__':
    maxLength = 0
    for d in xrange(2,1001):
        try:
            newLength = len(getRepeatingCycleFromFraction(1/Decimal(d)))
        except:
            newLength = 0
        if newLength>maxLength:
            maxD = d
            maxLength = newLength
    print maxLength
    print maxD
