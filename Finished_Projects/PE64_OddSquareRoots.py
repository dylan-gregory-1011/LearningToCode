#!/usr/bin/env python
"""finished on 3/1/2018: This gets all the values that have an odd period for the continued
fraction from the squared roots.  Struggled with the precision that python carries with decimals when
building the continued fraction.

def getFractionRepresentation(int) -> [int, [int]] : This function gets the continued fraction of a
number along with the initial term.

def checkForIteratingSequence([int]) -> Boolean: Tthis function checks to find the repeating sequence of a
continued fraction.  It first checks to see if the fraction is one repeating number and if it isnt,
then we check to find if a phrase is repeating and confirm it for a variable amount of times based on the amount
of terms that we trust python's precision

def createArrayOfSquaredValues(int) -> [int]: This is a function that calculates all of the possible
squared values beneath a maximum value.

"""

from decimal import *
from fractions import Fraction
from math import sqrt,pow
getcontext().prec = 1000

__author__ = "Dylan Smith"
__copyright__ = "Copyright (C) 2018 Dylan Smith"
__credits__ = ["Dylan Smith"]

__license__ = "Public Domain"
__version__ = "1.0"
__maintainer__ = "Dylan Smith"
__email__ = "-"
__status__ = "Development"

def getFractionRepresentation(number):
    fractionOfNumber = Fraction(Decimal(number))
    a0 = fractionOfNumber.numerator // fractionOfNumber.denominator
    iteratingDenominator = fractionOfNumber.numerator - fractionOfNumber.denominator*a0
    iteratingNumerator = fractionOfNumber.denominator
    sequence = []
    for iterations in  xrange(0,500):
        newFactor = iteratingNumerator  // iteratingDenominator
        sequence.append(newFactor)
        tempNumerator = iteratingNumerator - newFactor*iteratingDenominator
        iteratingNumerator, iteratingDenominator = iteratingDenominator, tempNumerator
        if iteratingDenominator == 1:
            sequence.append(iteratingNumerator)
            break
    return [a0, sequence]

def checkForIteratingSequence(arrayOfFractionality):
    incrementingIndex, repeatingSequenceFound = 2, False
    while repeatingSequenceFound == False and incrementingIndex < len(arrayOfFractionality):
        repeatingSequence = arrayOfFractionality[0:incrementingIndex]
        if len(set(repeatingSequence)) == 1:
            if incrementingIndex == 10:
                return [repeatingSequence[0]]
        else:
            repeatingSequenceFound = True
            if incrementingIndex < 20:
                amountOfRepetitionsNeeded = 4
            elif incrementingIndex >= 20 and incrementingIndex<30:
                amountOfRepetitionsNeeded = 3
            else:
                amountOfRepetitionsNeeded = 2
            for factorIncrement in xrange(1,amountOfRepetitionsNeeded):
                offsetFactor = incrementingIndex*factorIncrement
                if repeatingSequence == arrayOfFractionality[offsetFactor:offsetFactor+len(repeatingSequence)]:
                     continue
                else:
                    repeatingSequenceFound = False
                    break
            if repeatingSequenceFound == True:
                return repeatingSequence
        incrementingIndex+=1


def createArrayOfSquaredValues(maxValue):
    squaredValues = []
    for x in xrange(1,maxValue+1):
        squaredValues.append(x**2)
    return squaredValues

if __name__ == '__main__':
    countOfFractions = 0
    setOfSquares = set(createArrayOfSquaredValues(100))
    for value in xrange(2,10001):
        if value in setOfSquares:
            continue
        array = getFractionRepresentation(Decimal(value).sqrt())[1]
        if len(checkForIteratingSequence(array)) % 2 !=0:
            countOfFractions+=1
    print countOfFractions
