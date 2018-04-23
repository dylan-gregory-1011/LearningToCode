#!/usr/bin/env python
"""solved on 4/16/2018: Made it
far more complex then it needed to be.
sort through the functions to what the partitioning returned"""

__author__ = "Dylan Smith"
__copyright__ = "Copyright (C) 2018 Dylan Smith"
__credits__ = ["Dylan Smith"]

__license__ = "Public Domain"
__version__ = "1.0"
__maintainer__ = "Dylan Smith"
__email__ = "-"
__status__ = "Development"

def calculateFactorialForNumber(n):
    if n>1:
        return n*calculateFactorialForNumber(n-1)
    else:
        return 1

def getFactorialsFromOneToTen():
    factorials = {'0':1}
    for number in xrange(1,10):
        factorials[str(number)] = calculateFactorialForNumber(number)
    return factorials

def getSumOfFactorials(number,factorials):
    return sum([factorials[digit] for digit in str(number)])

if __name__  == '__main__':
    factorials = getFactorialsFromOneToTen()
    count = 0
    for x in xrange(145,1500000):
        if getSumOfFactorials(x, factorials) == x:
            count+=x
    print count
