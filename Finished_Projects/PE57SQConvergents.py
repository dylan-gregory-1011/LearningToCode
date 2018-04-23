#!/usr/bin/env python
"""completed on 3/5/2018: Find the amount of numbers that have a convergent term with a numerator
greater then their denominator.  For each factor, work backwords from the furthest decimal in the denominator
and get the current working convergent sum.  With this term convert it to a Fraction and check the numerator and denominator.

func getConvergentFraction(list, int) -> Fraction: Find the convergent fraction term for the int term.

func getSqrtOfTwoFraction() -> list : Get an array of the list of the denominator of the square root of two.

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

def getConvergentFraction(continued_fraction, term_to_get):
    convergentFraction = Fraction(1/Decimal(continued_fraction[term_to_get - 1]))
    for fractionIndex in xrange(term_to_get - 2, 0,-1):
        convergentFraction = 1 / (continued_fraction[fractionIndex] + convergentFraction)
    return Fraction(str(continued_fraction[0] + convergentFraction))

def getSqrtOfTwoFraction():
    continued_fraction = [1]
    for x in xrange(0,1000):
        continued_fraction.append(2)
    return continued_fraction

if __name__ == '__main__':
    continued_fraction_of_two = getSqrtOfTwoFraction()
    convergent_numerators_sum = 0
    for iteration in xrange(2,1002):
        convergentTerm = getConvergentFraction(continued_fraction_of_two, iteration)
        if len(str(convergentTerm.numerator)) > len(str(convergentTerm.denominator)):
            convergent_numerators_sum +=1
    print convergent_numerators_sum
