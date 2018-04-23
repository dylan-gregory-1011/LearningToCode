#!/usr/bin/env python
"""finished on 2/1/2018: check all the values between 3 and 1,000,000 to see if they have a repeating cycle of
length 60. It continues to check every value's repeating sequence and if it gets to 61 then it increments the max
counter and moves on to the next function

Answer: """

import csv
from collections import defaultdict

__author__ = "Dylan Smith"
__copyright__ = "Copyright (C) 2018 Dylan Smith"
__credits__ = ["Dylan Smith"]

__license__ = "Public Domain"
__version__ = "1.0"
__maintainer__ = "Dylan Smith"
__email__ = "-"
__status__ = "Development"

#ensures that the primes are
def int_wrapper(reader):
    for v in reader:
        yield map(int, v)

def getPrimesLessThan(maxNumber):
    #download the fist 1 to x primes from the excel list that are less then the max number
    with open('C:\\Users\\dylan smith\\Documents\\Python\\Project_Euler\\primes.csv') as prime_csv:
        primes = [number for row in int_wrapper(csv.reader(prime_csv)) for number in row if number<maxNumber]
    return primes

#check each prime for sub primes.  Iterate through every combination of numbers in the prime value and build an array of all the combinations of sub primes that are available
def checkPrimesForSubPrimes(prime, setOfPrimes):
    foundValue = []
    strOfPrime = str(prime)
    for strIndex in xrange(1,len(strOfPrime)):
        if (int(strOfPrime[:strIndex]) in setOfPrimes) and ((int(strOfPrime[strIndex:]) in setOfPrimes) and strOfPrime[strIndex:][0] !='0'):
            foundValue.append((int(strOfPrime[:strIndex]),int(strOfPrime[strIndex:])))
    if len(foundValue) == 0:
        return [(0,0)]
    else:
        return foundValue

#get the intersection of two lists.  Make each a set before converting back to a list to improve performance
def intersect(a, b):
    """ return the intersection of two lists """
    return list(set(a) & set(b))

#Iterate through the prime arrays to ensure that a sequence of primes is all concatenable
def iterateThroughMatchingSets(currentMatchingPrimes, dictOfPrimes,primeValueArray, previousValue):
    #limit the prime value array to values that are less then the function call's previous value.  Since the prime array is sorted then we know that we are
    #keeping the prime array to only include values for the current iteration.
    primeValueArray = [x for x in primeValueArray if x< previousValue]
    primeValueArray.append(previousValue)

    #if there is no values left to match then return the prime array that has been built by this iteration
    if len(currentMatchingPrimes) == 0:
        return primeValueArray

    #for each input of current matching primes, iterate over each value and run the same function on the intersection of the remaining primes.  When the values
    #is in the prime dictionary, call the recursive function.  Print out only values that have a length of x
    for value in sorted(currentMatchingPrimes):
        if value in dictOfPrimes.keys():
            finalValueArray = iterateThroughMatchingSets(intersect(dictOfPrimes[value],currentMatchingPrimes), dictOfPrimes, primeValueArray, value)
        try:
            if len(finalValueArray)==5:
                print sum(finalValueArray)
                print finalValueArray
        except:
            continue

#sort the keys for each array so you can increment numerically and call the set matching function for each value to be the initial value
def getPrimeConcats(dictOfPrimes):
    sortedKeyArray = sorted([keys for keys in dictOfPrimes.keys()])
    print "array has been sorted"
    futureFactorsList = []
    for index,keys in enumerate(sortedKeyArray):
        finalValueArray = iterateThroughMatchingSets(dictOfPrimes[keys], dictOfPrimes, [], keys)

#build a dictionary of primes and the values that it is concatenable with.  Also built a set of primes from the array of primes to allow for quicker lookups
#check each prime for a sub prime and then iterate through the array and add the smaller prime as a key and larger as a value if it doesn't exist
#or append the value onto an existing array if the key already exists.
def buildPrimeFactorDict():
    arrayOfPrimes = getPrimesLessThan(90000000)
    setOfPrimes = set(arrayOfPrimes)
    arrayOfPrimeFactors, concatenatedPrimes = set(),defaultdict(list)
    print "array has been built"
    for primeValue in arrayOfPrimes:
        tupleOfPrimes =  checkPrimesForSubPrimes(primeValue, setOfPrimes)

        for primeTuple in tupleOfPrimes:
            sortedPrimeTuple = tuple(sorted(primeTuple))
            if sortedPrimeTuple != (0, 0) and sortedPrimeTuple in arrayOfPrimeFactors:
                if sortedPrimeTuple[0] in concatenatedPrimes.keys():
                    concatenatedPrimes[sortedPrimeTuple[0]].append(sortedPrimeTuple[1])
                else:
                    concatenatedPrimes[sortedPrimeTuple[0]] = [sortedPrimeTuple[1]]
                    continue
            elif sortedPrimeTuple != (0, 0) :
                arrayOfPrimeFactors.add((sortedPrimeTuple))
    return concatenatedPrimes

if __name__ == '__main__':
    primeFactorDict = buildPrimeFactorDict()
    print "dictionary has been built"
    getPrimeConcats(primeFactorDict)
