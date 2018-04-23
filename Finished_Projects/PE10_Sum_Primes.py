import csv
from binomial_reps import int_wrapper
primes  =[]
with open('primes.csv') as prime_list:
      reader = csv.reader(prime_list)
      reader = int_wrapper(reader)
      for row in reader:
          primes.append(row[0])
len_prim = len(primes)
i = 0
sum_primes = 0
while primes[i]<2000000:
    sum_primes+=primes[i]
    i+=1
print primes[len_prim-1]
print sum_primes
