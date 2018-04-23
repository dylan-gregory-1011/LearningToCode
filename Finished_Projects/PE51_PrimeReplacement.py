#!/usr/bin/env python
"""finished on 2/19/2018: Something about prime families
"""

import csv
import re

__author__ = "Dylan Smith"
__copyright__ = "Copyright (C) 2017 Dylan Smith"
__credits__ = ["Dylan Smith"]

__license__ = "Public Domain"
__version__ = "1.0"
__maintainer__ = "Dylan Smith"
__email__ = "-"
__status__ = "Development"

file_for_primes = '\\PATH\\TO\\FILE\\primes.csv'
#ensures that the primes are
def int_wrapper(reader):
    for v in reader:
        yield map(int, v)

def getPrimesLessThan(maxNumber):
    #download the fist 1 to x primes from the excel list that are less then the max number
    with open(file_for_primes) as prime_csv:
        primes = [str(number) for row in int_wrapper(csv.reader(prime_csv)) for number in row if number<maxNumber]
    return primes

def checkIfMoreThenOneSimilarValue(number):
    #create a dictionary of values and ensure that there are similar numbers
    # in the prime and to record down the index
    numbers = {}
    matching = False
    for index, value in enumerate(number):
        if index + 1 == len(strOfNumber):
            break
        try:
            numbers[value].append(index)
            if int(value)<=2:
                matching =  True
        except:
            numbers[value] = [index]
    #if the values are matching then return the numbers that have multiple indices.
    if matching:
        return {k: v for k, v in dictOfNumbers.iteritems() if len(v)>1}

def iterateThroughValues(multiples, number, primes):
    #iterate through the dictionary of indicies that can be replaced with differing values.
    #if the length is 2 then check the prime family of the number, else if there is three then
    #check if all three make a prime family and also check if any variation of two of the three makes one.
    for keys in multiples.keys():
        if len(multiples[keys]) == 2:
            if checkPrimeFamily(multiples[keys], number, primes):
                print number
                return True
        else:
            values = multiples[keys]
            if checkPrimeFamily(values, strOfNumber, primes):
                print number
                return True

            for index,value in enumerate(values[:-1]):
                for index1, value1 in enumerate(values[index + 1:]):
                    if checkPrimeFamily([value,value1], number, primes):
                        print number
                        return True
    return False

#check if iterations of the same number are all of the same prime family.  if enough non primes are found then break
def checkPrimeFamily(arrayOfIndexValues, strOfNumber,setOfPrimes):
    nonFamilyCount = 0
    arrayOfTheNumber = list(strOfNumber)
    for replaceValue in xrange(0,10):
        for value in arrayOfIndexValues:
            arrayOfTheNumber[value] = str(replaceValue)
        if "".join(arrayOfTheNumber) not in setOfPrimes:
            nonFamilyCount +=1

        if nonFamilyCount==3:
            return False
    return True

if __name__ == '__main__':
    arrayOfPrimes = getPrimesLessThan(1000000)
    setOfPrimesAsString = set(arrayOfPrimes)

    for prime in arrayOfPrimes:
        try:
            dictOfPrimes = checkIfMoreThenOneSimilarValue(prime)
            if iterateThroughValues(dictOfPrimes, prime, setOfPrimesAsString):
                break
        except:
            pass
