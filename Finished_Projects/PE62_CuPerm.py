#!/usr/bin/env python
"""finished on 10/2/2017: Check to see how many number + power combinations with both values as less then 10
have the same number of digits as the power. Tterate through the powers and append the count until a number is found
that does not match the length of the power. once this is done move on to the next numberIterator

func permutationCheckFor(int) -> dictionary : function creates a dictionary, one number with the amount of
decimals in the original number and then the number that dictates the permutations with the number of each
number in the corresponding place #0s#1s#2s#3s, etc

func checkCube(int, list, int) -> int : this function checks the cube in question and iterates over
the array to see how many permutations are there.

"""

__author__ = "Dylan Smith"
__copyright__ = "Copyright (C) 2017 Dylan Smith"
__credits__ = ["Dylan Smith"]

__license__ = "Public Domain"
__version__ = "1.0"
__maintainer__ = "Dylan Smith"
__email__ = "-"
__status__ = "Development"

def permutationCheckFor(number):
    numStr = str(number)
    newNum = ''
    for x in xrange(0,10):
        counter = 0
        for y in numStr:
            if x == int(y):
                counter+=1
        newNum += str(counter)
    newDict = {}
    newDict[len(numStr)] = float(newNum)
    return newDict

def checkCube(cube, Array, start):
    counter = 0
    for y in xrange(start, len(Array)):
        if cube.keys()[0] < Array[y].keys()[0]:
            break
        if cube.values()[0] == Array[y].values()[0]:
            counter += 1
    return counter

if __name__ == '__main__':
    cubePermutations = []
    #create an array of the permutations and their breakdown
    for x in xrange(0,10000):
        cubePermutations.append(permutationCheckFor(x**3))
    #this keeps track of the starting index point and the current length
    curStart = 0
    curLength = 0
    #iterates over the cube testing each permutation.
    for idx, cube in enumerate(cubePermutations):
        #if the length of the number is longer, bump up the incrementer so as to ensure it only operates
        #over the intended range
        if cube.keys()[0]> curLength:
            curLength +=1
            curStart = idx
        count = checkCube(cube, cubePermutations, curStart)
        if count == 5:
            print idx**3
            break
