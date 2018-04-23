#!/usr/bin/env python
"""finished on 7/11/2017: Find the first value where a number and a multiple of itself are permutations.
Increment i and multiple i by x (2->7) until the first permutation is reachedself.

func circularPrimesCheck(int, [int]) -> boolean : Check if a circular iteration of the prime
is also a prime.  Make sure all iterations are prime 

Answer: 55
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

prime_file_input = 'C:\\Users\\uscdxs92\\Documents\\Python\\Project_Euler\\primes.csv'

def int_wrapper(reader):
    for v in reader:
        yield map(int, v)

def circularPrimesCheck(prime, primes):
    prime_str = str(prime)
    circ_prime = True
    for x in xrange(0,len(prime_str)-1):
        prime_str = prime_str[1:]+ prime_str[0]
        if int(prime_str) in primes:
            continue
        circ_prime = False
        break
    return circ_prime

def getPrimesLessThan(maxNumber):
    with open(prime_file_input) as prime_csv:
        primes = [number for row in int_wrapper(csv.reader(prime_csv)) for number in row if number<maxNumber]
    return primes

if __name__ == '__main__':
    primes = getPrimesLessThan(1000000)
    total = 0
    for prime_num in primes:
        if circularPrimesCheck(prime_num, primes):
            total+=1
    print total
