#!/usr/bin/env python
"""finished on 6/20/2017: Find three prime values that are all permutations of each other.  these values need
to have 4 digits each so only primes between 1000 and 9999 are valid.  Concatenate ones that are permutations of each other

func rearrangePermutation(int) -> int: rearranges the digits in a number in order and returns this number

func checkIfPermutations(int, int) -> boolean : Check if two numbers are permutations of each other.  It compares
the output of the function above and if they are the same number the values are permutations

Answer: 296962999629
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

file_for_primes = 'C:\\Users\\uscdxs92\\Documents\\Python\\Project_Euler\\primes.csv'

def getPrimesLessThan(maxNumber):
    #download the fist 1 to x primes from the excel list that are less then the max number
    with open(file_for_primes) as prime_csv:
        primes = [number for row in int_wrapper(csv.reader(prime_csv)) for number in row if number<maxNumber and number>1000]
    return primes

#use this function to download primes as integers from the file we have.
def int_wrapper(reader):
    for v in reader:
        yield map(int, v)

#create a string of all the numbers arranged in order.  This will be used to check for permutations
def rearrangePermutation(number):
    return ''.join([str(y) for y in sorted([int(x) for x in str(number)])])

def checkIfPermutation(number_one, number_two):
    if rearrangePermutation(number_one) == rearrangePermutation(number_two):
        return True
    else:
        return False

if __name__ == '__main__':
    primes = getPrimesLessThan(9999)
    for ix in xrange(0,len(primes)):
        for jx in xrange(ix+1, len(primes)):
            #if these first two primes are not permutations, move on to the next prime
            if not checkIfPermutation(primes[jx], primes[ix]):
                continue
            #if they are permutations then calculate the next prime in the list based on the difference and then check to see if that number
            #is a prime and if it is a permutation of the first.  Print the numbers where this is a case.
            new_number = primes[jx]+ (primes[jx] - primes[ix])
            if new_number in primes and checkIfPermutation(primes[ix],new_number):
                print str(primes[ix])+str(primes[jx])+str(new_number)
                break
