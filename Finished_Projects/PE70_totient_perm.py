#!/usr/bin/env python
"""finished on 1/11/2018: Iterate over the range of values given by the problem.
Once we have the eulers value we check to see if the value is less then the min value.
If this is the case then we check to see if it is a permutation.  If it is we reset the min value. and continueself.

func rearrangePermutation(int) -> int: rearranges the digits in a number in order and returns this number

func checkIfPermutations(int, int) -> boolean : Check if two numbers are permutations of each other.  It compares
the output of the function above and if they are the same number the values are permutations

func binarySearch(array, number) -> index: To find the totient, we use a binary search of the prime values that looks at a list and returns the value that is closest to the item.
It splits the list in half by index and checks the value. It keeps splitting the list in half until it finds
the correct value

func getEulerQuotient(int, Set, list) -> int: this function checks to make sure the value is not a prime,
and then gets the initial prime index which represents the number around the values sqrt.  Once we have this we
check for the first prime that is in the value.  If this value multiplied with one other prime
gives us the value then we get the euluer quotient value.  If not, the value is inconsequential and we return 1

"""

import csv
from math import floor, sqrt

__author__ = "Dylan Smith"
__copyright__ = "Copyright (C) 2018 Dylan Smith"
__credits__ = ["Dylan Smith"]

__license__ = "Public Domain"
__version__ = "1.0"
__maintainer__ = "Dylan Smith"
__email__ = "-"
__status__ = "Development"

prime_file_path = 'C:\\Users\\uscdxs92\\Documents\\Python\\Project_Euler\\primes.csv'

#used to get a list of primes as integers
def int_wrapper(reader):
    for v in reader:
        yield map(int, v)

#create a string of all the numbers arranged in order.  This will be used to check for permutations
def rearrangePermutation(number):
    return ''.join([str(y) for y in sorted([int(x) for x in str(number)])])

#returns true if the value is a permutation of the other, else returns false.
def checkIfPermutation(number, eulersTotient):
    if rearrangePermutation(number) == rearrangePermutation(eulersTotient):
        return True
    else:
        return False

#this function returns an array and set of primes.  The set allows for quicker lookup times and the
#array allows to iterate over similar values.
def returnArrayOfPrimes():
    primeSet  = set()
    primeArray = []
    with open(prime_file_path) as prime_csv:
        reader = int_wrapper(csv.reader(prime_csv))
        for row in reader:
            for value in row:
                primeSet.add(value)
                primeArray.append(value)
    return primeArray, primeSet


def binarySearch(anArray, item):
    first = 0
    last = len(anArray)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if anArray[midpoint-1] < item and anArray[midpoint+1] > item:
            found = True
        else:
            if item < anArray[midpoint+1] and item < anArray[midpoint - 1]:
                last = midpoint-1
            else:
                first = midpoint+1

    return midpoint


def getEulerQuotient(value, primeSet, primeArray):
    if value in primeSet:
        return value - 1

    initialPrimeIndex = binarySearch(primeArray,floor(sqrt(value)))

    while initialPrimeIndex>1:
        if value % primeArray[initialPrimeIndex] != 0:
            initialPrimeIndex -= 1
            continue
        if  (value / primeArray[initialPrimeIndex]) in primeSet and value != primeArray[initialPrimeIndex]:
            return (primeArray[initialPrimeIndex] - 1)* ((value / primeArray[initialPrimeIndex]) - 1)
        else:
            return 1.00

    return 1

if __name__ == '__main__':
    #create an array with primes less then 10,000,000
    primeArray, primeSet = returnArrayOfPrimes()
    minValue = float(87109)/float(79180)

    for x in xrange(2,10**7):
        euluersValue = getEulerQuotient(x, primeSet, primeArray)

        if float(x)/float(euluersValue) < minValue:
            if checkIfPermutation(x,euluersValue):
                minValue = float(x)/float(euluersValue)
                minNumber = x

    print minValue
    print minNumber
