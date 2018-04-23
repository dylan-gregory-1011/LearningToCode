#!/usr/bin/env python
"""finished on 7/1/2017: Check all the values between 3 and 1,000,000 to see if they have a repeating cycle of
length 60. It continues to check every value's repeating sequence and if it gets to 61 then it increments the max
counter and moves on to the next function

func findFactorialsBelow(int) -> {str: int} : get the factorials for the numbers

func getRepeatingSequenceFor([int], int, {str: int}) -> gets the repeating sequence for a value

"""

__author__ = "Dylan Smith"
__copyright__ = "Copyright (C) 2017 Dylan Smith"
__credits__ = ["Dylan Smith"]

__license__ = "Public Domain"
__version__ = "1.0"
__maintainer__ = "Dylan Smith"
__email__ = "-"
__status__ = "Development"

#create a dictionary that has all of the factorial values from 0-9 in a dictionary.
def findFactorialsBelow(max_number):
    factorials = {}
    for x in xrange(0,max_number):
        factorials[str(x)] = factorial(x)
    return factorials

#calculates the factorial for each number
def factorial(num):
    if num >1:
        return num*factorial(num-1)
    elif num == 0:
        return 1
    elif num == 1:
        return 1

#this function takes the current number in the cycle (next_num), an array of all numbers in the cycle, and the factorial dict
#it calculates what the next number will be and check to see if it is in the array.  if it is, an empty array is returned
def getRepeatingSequenceFor(next_number, array,factorials):
    old_value = str(next_number)
    next_value = sum([factorials.get(x) for x in old_value])
    if next_value in array:
        return [] , next_value
    else:
        array.append(next_value)
        return array, next_value

if __name__ == '__main__':
    max_count = 0
    factorials = findFactorialsBelow(10)

    for x in xrange(3,1000000):
        counter = 1
        repeating_sequence = [x]
        next_value = x
        while len(repeating_sequence) != 0:
            repeating_sequence, next_value = getRepeatingSequenceFor(next_value, repeating_sequence, factorials)
            counter += 1
        if counter ==61:
            max_count+=1
    print max_count
