#!/usr/bin/env python
"""finished on 3/3/2018: Since we only need the 100th convergence then we get 100 terms of the continued
fraction and plug this calculation into the convergent fraction mentioned above.
 We then create a string of the numerator and sum all of the terms.

def getContinuedFractionOfE(int) -> [int] : Returns the continued fraction for e with length of the
input.

def getConvergentFraction([int], int) -> Fraction: This gets the continued fraction for the term
that is specified. It accomplishes this by working backwards from the term and then
continuously appending this value to previous values

"""

from decimal import *
from fractions import Fraction
from math import sqrt,pow, e
getcontext().prec = 100

__author__ = "Dylan Smith"
__copyright__ = "Copyright (C) 2018 Dylan Smith"
__credits__ = ["Dylan Smith"]

__license__ = "Public Domain"
__version__ = "1.0"
__maintainer__ = "Dylan Smith"
__email__ = "-"
__status__ = "Development"

def getContinuedFractionOfE(maxNumberOfCoefficients):
    convergingSequence = [2,1]
    for k in xrange(1,maxNumberOfCoefficients):
        convergingSequence.append(2*k)
        convergingSequence.append(1)
        convergingSequence.append(1)
    return convergingSequence

def getConvergentFraction(continuedFraction, termToGet):
    convergentFraction = Fraction(1/Decimal(continuedFraction[termToGet - 1]))
    for fractionIndex in xrange(termToGet - 2, 0,-1):
        convergentFraction = 1 / (continuedFraction[fractionIndex] + convergentFraction)
    return Fraction(str(continuedFraction[0] + convergentFraction))

if __name__ == '__main__':
    continuedFractionOfE = getContinuedFractionOfE(40)
    numeratorOfTerm = getConvergentFraction(continuedFractionOfE, 100).numerator
    sumOfTerms = 0
    for number in str(numeratorOfTerm):
        sumOfTerms += int(number)
    print sumOfTerms
