#!/usr/bin/env python
"""finished on 6/22/2017: Find the maximum value created when a number is divided by its totients. Iterate over all
possible values skipping prime numbers and compare the values to the most recent maximum.

func getPhiForEuelersTotient(int, list) -> int: Get the phi value for each value by using all of its prime factors.

func findPrimeFactorsFor(int, list) -> list: factor each number and return the array of prime factors

"""

import csv

__author__ = "Dylan Smith"
__copyright__ = "Copyright (C) 2017 Dylan Smith"
__credits__ = ["Dylan Smith"]

__license__ = "Public Domain"
__version__ = "1.0"
__maintainer__ = "Dylan Smith"
__email__ = "-"
__status__ = "Development"

prime_file_path = 'C:\\Users\\uscdxs92\\Documents\\Python\\Project_Euler\\primes.csv'
def int_wrapper(reader):
    for v in reader:
        yield map(int, v)

def getPhiForEuelersTotient(num, factors):
    phi = float(num)
    for prime in factors:
        phi = phi*(1-1/float(prime))
    return phi

def findPrimeFactorsFor(num, primes):
    divisors = []
    prime_found = 0
    for ix in xrange(0,len(primes)):
        if num%primes[ix] == 0:
            num = num/primes[ix]
            divisors.append(primes[ix])
            prime_found +=1
        if ix == 1 and prime_found ==0 :
            break
        if ix >100:
            divisors = []
            break
        if num == 1 :
            break
    return divisors

if __name__ == '__main__':
    #create an array with primes less then 1,000,000
    with open(prime_file_path) as prime_csv:
        reader = int_wrapper(csv.reader(prime_csv))
        primes = [row[0] for row in reader if row[0]< 1001000]
    max_totient = 2.0000
    prime_array =[]
    ix = 0
    #iterate over all values less then 100000 and check to find the max totient.  Slowly build an array of the latest current prime_arr
    #to cut out iterating each time and if the number is a prime the skip to the next number and add it to the list
    for n in xrange(1,1000000):
        while n>primes[ix]:
            ix+=1
        if n == primes[ix]:
            prime_array.append(n)
            pass
        #get the factors of the number.  If an empty array then skip.  This allows for only calculating optimal totient.
        factors = findPrimeFactorsFor(n,prime_array)
        if len(factors) == 0:
            pass
        #calculate phi and increment if the new totient is greater then previous totients.
        phi = getPhiForEuelersTotient(n,factors)
        if float(n)/float(phi) > max_totient:
            max_totient = float(n)/float(phi)
            print max_totient
            print n
