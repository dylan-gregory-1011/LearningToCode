#!/usr/bin/env python
"""finished on 6/30/2017: for every value of n (skip those divisible by two, the remainder
is 2), check the value and see how long the remainder is. if greater than 10**10, breakself.
"""

import csv
#from pe import sieve

__author__ = "Dylan Smith"
__copyright__ = "Copyright (C) 2017 Dylan Smith"
__credits__ = ["Dylan Smith"]

__license__ = "Public Domain"
__version__ = "1.0"
__maintainer__ = "Dylan Smith"
__email__ = "-"
__status__ = "Development"

prime_file_input = '\\PATH\\TO\\FILE\\\\primes.csv'

def int_wrapper(reader):
    for v in reader:
        yield map(int, v)

if __name__ == '__main__':
    #download the primes list
    with open(prime_file_input) as prime_csv:
        reader = int_wrapper(csv.reader(prime_csv))
        primes = [row[0] for row in reader if row[0] < 1000000]

    #  Optimal code is below which uses a different equation
    for i in xrange(1,len(primes),2):
        curr_prime = primes[i-1]
        val = ((curr_prime-1)**i + (curr_prime+1)**i) % curr_prime**2
        if val>10**10:
            print i
            break
    print "prime is %i" % curr_prime
    print 'value of i is %i' % i

#You don't need to calculate (2*(n+1)*p[n])%(p[n]*p[n]). We showed in Problem 120 that
#(2*(n+1)*p[n])%(p[n]*p[n] will be equal to 2 when
#n+1 is even and will be equal to 2(n+1)*p[n] when n+1 is odd.
def optimal_code():
    p = sieve(1000000)

    for n in xrange(7038, len(p), 2):
	    if 2*(n+1)*p[n] > pow(10,10):
		    print n+1
		    break
