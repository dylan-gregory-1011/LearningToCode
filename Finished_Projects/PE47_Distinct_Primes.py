#!/usr/bin/env python
"""finished on 6/21/2017: Try to find the number that begins a sequence of four consecutive numbers with
four distinct prime factors

func countOfDistinctPrimeFactors(int, [int]) -> int : takes a number and the list of primes and iterates
over the prime values to find the divisors of the number.  Every time a new distinct divisor is found the counter
is incremented

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

file_for_primes = '\\PATH\\TO\\FILE\\primes.csv'

def int_wrapper(reader):
    for v in reader:
        yield map(int, v)

def getPrimesLessThan(maxNumber):
    with open(file_for_primes) as prime_csv:
        primes = [number for row in int_wrapper(csv.reader(prime_csv)) for number in row if number<maxNumber]
    return primes

def countOfDistinctPrimeFactors(number, primes):
    divisor_count, previous_prime = 0, 0
    for ix in xrange(0,len(primes)):
        if number%primes[ix] == 0:
            number = number/primes[ix]
            if primes[ix]!= previous_prime:
                divisor_count+=1
                previous_prime = primes[ix]
            continue
        if num == 1 or divisor_count >= 5:
            break
    return divisor_count

if __name__ == '__main__':
    primes = getPrimesLessThan(10000)
    counter = 0
    #iterate through all the numbers and see how many distinct prime factors each has.  If we find one with four then increment the counter and move to the next
    #one.  If one doesnt have four then start back at zero and move on regardless.
    for num in xrange(1, 1000000):
        if countOfDistinctPrimeFactors(num, primes) == 4:
            counter+=1
            if counter == 4:
                print num - 3
                break
        else:
            counter = 0
