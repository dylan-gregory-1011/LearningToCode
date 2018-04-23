#!/usr/bin/env python
"""finished on 1/10/2018: Check to see how many number + power combinations with both values as less then 10
have the same number of digits as the power. Tterate through the powers and append the count until a number is found
that does not match the length of the power. once this is done move on to the next numberIterator

func checkNumberForDigits(int, int) -> boolean : checks if the value returned from multiplying a power and number has the
same length as the power

"""

__author__ = "Dylan Smith"
__copyright__ = "Copyright (C) 2018 Dylan Smith"
__credits__ = ["Dylan Smith"]

__license__ = "Public Domain"
__version__ = "1.0"
__maintainer__ = "Dylan Smith"
__email__ = "-"
__status__ = "Development"

#We check to ensure that the number to the power has the same legnth as the power
def checkNumberForDigits(number , power):
    if len(str(number**power)) == power:
        return True
    else:
        return False

if __name__ == '__main__':
    #set the initial count and power number.
    count = 0
    #iterate from 1-10 checking each number and iterating through a ragne of powers
    for numberIterator in xrange(1,10):
        powerIterator = 1
        while checkNumberForDigits(numberIterator, powerIterator):
            count+=1
            powerIterator+=1
        print "Count after %i is %i" % ( numberIterator, count)
