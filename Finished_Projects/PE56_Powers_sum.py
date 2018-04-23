#!/usr/bin/env python
"""finished on 8/4/2017: Find the maximum sum of the powers a,b < 100.  Check this function to ensure that the formula is
correct.

func convertNumberToArray(int) -> [int]: breaks the integer into a list of its components.

func multiplicationOfTwoValues([int], [int]) -> [int]: function that mimics basic multiplication.  Iterates over all the possible
values and adds to the next number in the series.

"""

__author__ = "Dylan Smith"
__copyright__ = "Copyright (C) 2017 Dylan Smith"
__credits__ = ["Dylan Smith"]

__license__ = "Public Domain"
__version__ = "1.0"
__maintainer__ = "Dylan Smith"
__email__ = "-"
__status__ = "Development"

def convertNumberToArray(num):
    array = [int(str(num)[0])]
    try:
        array.append(int(str(num)[1]))
    except:
        pass
    return array

def multiplicationOfTwoValues(previous_number, multiplier):
    multiplier_ix =  len(multiplier) - 1
    #set the first multiple using only the singles digit.  Get the next number and the "carry over"
    next_value = previous_number[len(previous_number) - 1]*multiplier[multiplier_ix]
    next_number = [next_value%10]
    incr = next_value//10
    #make your way through the two numbers.  Apply common multiplication logic
    for ix in xrange(len(previous_number) -1 ,0, -1):
        #work from right to left.  Need a try except to handle the index issues of single digit multiplication
        try:
            #add the increment and two multiples to the next value.  Increment this value to be the next number, get the carry over and move on
            next_value = previous_number[ix-1]*multiplier[multiplier_ix] + previous_number[ix]*multiplier[multiplier_ix-1] + incr
        except:
            next_val = previous_number[ix]*multiplier[multiplier_ix] + incr

        next_number, incr = [next_value%10] + next_number, next_value // 10
    #return the array of the next number
    return  convertNumberToArray(incr + multiplier[0]*previous_number[0]) + next_number

if __name__ == '__main__':
    max_power = 0
    for a in xrange(2,100):
        calculated_number = convertNumberToArray(a)
        power = calculated_number[:]
        for b in xrange(2,100):
            calculated_number = multiplicationOfTwoValues(calculated_number, power)
            if sum(calculated_number) > max_power:
                max_power = sum(calculated_number)

    print max_power
