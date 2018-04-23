from prime_functions import prime_factorization, int_wrapper
import csv
primes = []
#open the csv that stores the first million prime vlaues using the csv reader and the int wrapper that makes all the values integers
#creates an array of primes
with open('primes.csv') as prime_list:
    reader = csv.reader(prime_list)
    reader = int_wrapper(reader)
    for row in reader:
        primes.append(row[0])

#utilizing the prime vactorization formula that we have we find the factors that create the values
num, factors = prime_factorization(primes, 600851475143)
print factors
print num
