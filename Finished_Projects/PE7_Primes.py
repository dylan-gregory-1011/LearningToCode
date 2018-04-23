import csv
from binomial_reps import int_wrapper
primes  =[]
with open('primes.csv') as prime_list:
      reader = csv.reader(prime_list)
      reader = int_wrapper(reader)
      for row in reader:
          primes.append(row[0])
len_prim = len(primes)
print primes[10000]
