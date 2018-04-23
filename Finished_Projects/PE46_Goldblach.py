#!/usr/bin/env python
"""finished on 9/30/2017: Find the first value where goldblachs conejecture is false.  increment by
increasing values and check all non prime values for Golblachs conjecture.

def calculateSquareFactor() -> [int]: calculate the factor that gets added to all of the primes in the array

func checkGoldblachsConjecture(int, int) -> boolean : This calculates whether a number meets Goldbachs conjecture.

"""

import csv

__author__ = "Dylan Smith"
__copyright__ = "Copyright (C) 2017 Dylan Smith"
__credits__ = ["Dylan Smith"]

__license__ = "Public Domain"
__version__ = "1.0"
__maintainer__ = "Dylan Smith"
__email__ = "-"
__status__ = "Development"

#transform each number into an integer
def int_wrapper(reader):
    for v in reader:
        yield map(int, v)

def getPrimesLessThan(maxNumber):
    with open('C:\\Users\\uscdxs92\\Documents\\Python\\Project_Euler\\primes.csv') as prime_csv:
        primes = [number for row in int_wrapper(csv.reader(prime_csv)) for number in row if number<maxNumber]
    return primes

def calculateSquareFactor():
    return [2*(x**2) for x in xrange(1,1001)]

def checkGoldblachsConjecture(num, primes_ix,primes, sqFactor):
    run, wrk_prime_ix = False , primes_ix - 1
    while not run and wrk_prime_ix>=0:
        ix_sq = 0
        factor = num - primes[wrk_prime_ix]
        while factor > sqFactor[ix_sq]:
            ix_sq += 1
        if factor == sqFactor[ix_sq]:
            run = True
            break
        wrk_prime_ix -= 1
    return run

#this function increments the odd numbers and checks to see if the Goldbach conjecture
#is met.  If the prime number is also a prime then it gets skipped.
if __name__ == '__main__':
    primes, primes_ix = getPrimesLessThan(1000000), 4
    sqFactor = calculateSquareFactor()

    for increment in xrange(9,10000,2):
        if primes[primes_ix] == increment:
            primes_ix +=1
            continue
        if not checkGoldblachsConjecture(increment, primes_ix, primes, sqFactor):
            break
    print increment
