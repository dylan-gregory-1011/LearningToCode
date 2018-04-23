#!/usr/bin/env python
"""finished on 2/22/2018: Find the length of the side of the square where the prime ratio of the corners is first
less the 0.1.  We use the Miller Rabin test for primality to check each corner if it is prime and then increment the counter.

func incrementNumbers(int, int) -> int : increments the cursor over the four corners for the current side length and tests
the corner if it is prime.

func millerRabinTestForPrimality(int) -> Boolean: Uses a sample of random numbers to calculate new x values and check if
the number is prime based on the associated value.  Be sure to review & function and >> 1 functions in python as well
as the sample function

"""

from random import sample
import sys

__author__ = "Dylan Smith"
__copyright__ = "Copyright (C) 2017 Dylan Smith"
__credits__ = ["Dylan Smith"]

__license__ = "Public Domain"
__version__ = "1.0"
__maintainer__ = "Dylan Smith"
__email__ = "-"
__status__ = "Development"

def incrementNumbers(cursor, increment):
    primeSum = 0
    for x in xrange(0,4):
        if millerRabinTestForPrimality(cursor):
            primeSum+=1
        cursor += increment
    return primeSum


def millerRabinTestForPrimality(n, k = 7):
    if n < 6:  # assuming n >= 0 in all cases... shortcut small cases here
      return [False, False, True, True, False, True][n]
    # should be faster than n % 2..... bitwise operator
    if n & 1 == 0:
       return False

    d,r = n-1, 0
    while d & 1 == 0:
        #d >> 1 (is the same as d//2^1)
        r, d = r + 1, d >> 1
    #the sample function: sample(population,k), returns k values that are randomly spread over the range listed.
    #it returns a k list of samples from the population.  For this we also use the min function to limit values
    for a in sample(xrange(2, min(n - 2, sys.maxint)), min(n - 4, k)):
        #use the power function to optimally calculate the new x
        x = pow(a,d,n)
        if x != 1 and x != n - 1:
            for s in xrange(1,r):
                x = pow(x,2,n)
                if x == 1:
                    return False
                elif x == n - 1:
                    a = 0
                    break
            if a:
                return False
    return True

if __name__ == '__main__':
    continueIterating = True
    sideLength, primeCount, cursor, totalDiag = 3,0, 3, 1

    while continueIterating:
        primeCount += incrementNumbers(cursor, sideLength - 1)
        totalDiag += 4
        cursor += ((4*(sideLength - 1)) + 2)
        sideLength +=2
        if  float(primeCount)/float(totalDiag) < 0.1:
            print sideLength - 2
            break
