#!/usr/bin/env python
"""finished on 7/11/2017: Find the first value where a number and a multiple of itself are permutations.
Increment i and multiple i by x (2->7) until the first permutation is reachedself.

func checkIfPermutations(int, int) -> boolean : Check if two numbers are permutations of each other.  It
creates a list of all the digits of the first and then iterates through the second re-moving one number each time.

"""

__author__ = "Dylan Smith"
__copyright__ = "Copyright (C) 2017 Dylan Smith"
__credits__ = ["Dylan Smith"]

__license__ = "Public Domain"
__version__ = "1.0"
__maintainer__ = "Dylan Smith"
__email__ = "-"
__status__ = "Development"

def checkIfPermutations(number_one, number_two):
    permutations = list(str(number_one))
    for x in str(number_two):
        if x in permutations:
            permutations.remove(x)
            continue
        else:
            return False
    return True

if __name__ == '__main__':
    found, i = False, 1
    while not found :
        for x in xrange(2,7):
            if not checkIfPermutations(i,i*x):
                break
            if x == 6:
                found = True
                print i
        i+=1
