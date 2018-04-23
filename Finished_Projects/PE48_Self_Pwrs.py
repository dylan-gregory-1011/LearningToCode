#!/usr/bin/env python
"""finished on 9/29/2017: Iterate over all the values between 1 and 1000 and return the right ten
digits for the summation of all the self powers

func getNextValueForPower(int) -> decimal : takes a value and returns only
the least ten digits for the solution to n**n

func moduloTenDigits(int) -> int : returns 10 digits of a number

Answer: 9110846700
"""

__author__ = "Dylan Smith"
__copyright__ = "Copyright (C) 2017 Dylan Smith"
__credits__ = ["Dylan Smith"]

__license__ = "Public Domain"
__version__ = "1.0"
__maintainer__ = "Dylan Smith"
__email__ = "-"
__status__ = "Development"

def getNextValueForPower(n):
    value = n
    for pwr in xrange(1, n):
        value = moduloTenDigits(value*n)
    return value

def moduloTenDigits(value):
    return value%10000000000

if __name__ == '__main__':
    #initialize the sum
    selfPowers = 0
    for x in xrange(1,1001):
        selfPowers = moduloTenDigits(selfPowers+getNextValueForPower(x))
    print selfPowers
