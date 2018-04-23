import csv

from binomial_reps import int_wrapper
primes  =[]
with open('C:\\Users\\dylan smith\\Documents\\Learnin\\Python\\Project_Euler\\primes.csv') as prime_list:
      reader = csv.reader(prime_list)
      reader = int_wrapper(reader)
      for row in reader:
          primes.append(row[0])
print primes.index(47623)
primes_add = []
prime_made = []
start_ind = 0
current_ind = 1
max_ind = 21
max_sum_prime = 0
while primes[start_ind]*2<1000000:
    sum_primes = 0
    current_ind = start_ind
    while sum_primes<1000000:
        sum_primes+=primes[current_ind]
        i = 0
        while primes[i]<=sum_primes and sum_primes<1000000:
            if primes[i]== sum_primes and current_ind+1 >max_ind:
                max_ind = current_ind+1
                max_sum_prime = sum_primes
                print max_ind
                print max_sum_prime
                break
            i+=1
        current_ind+=1
    start_ind+=1
print max_ind
print max_sum_prime
