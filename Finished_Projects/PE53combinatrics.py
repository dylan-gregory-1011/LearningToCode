#!/usr/bin/env python
"""finished on 2/28/2018: this function gets
combinations by incrementing each step of the
way through the combination factors"""

__author__ = "Dylan Smith"
__copyright__ = "Copyright (C) 2018 Dylan Smith"
__credits__ = ["Dylan Smith"]

__license__ = "Public Domain"
__version__ = "1.0"
__maintainer__ = "Dylan Smith"
__email__ = "-"
__status__ = "Development"

def getCombinationOf(n,r):
    combination = 1.0000
    for d in xrange((n-r),0,-1):
        combination = combination*(float(n)/float(d))
        n-=1
    return combination

#iterate through all values of n and all values of c that are smaller then n and
# check to see if the combination is greater then a million
if __name__ == '__main__':
    distinct_values_greater_then = 0
    for n in xrange(2,101):
        for r in xrange(1,n):
            if getCombinationsOf(n,r) > 1000000:
                distinct_values_greater_then+=1
    print distinct_values_greater_then
