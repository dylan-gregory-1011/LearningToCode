import numpy as np
import csv
from math import sqrt


def int_wrapper(reader):
    for v in reader:
        yield map(int, v)

primes = []
#np.savetxt("primes.csv", primes)
with open('C:\\Users\\dylan smith\\Documents\\Learnin\\Python\\Intermediate_Python\\primes.csv') as prime_list:
    reader = csv.reader(prime_list)
    reader = int_wrapper(reader)
    for row in reader:
        primes.append(row[0])

#this function checks if each number is prime and if it is not equal to one.
#it returns one if prime, zero if not prime
def check_prime(num):
    ix = 0
    prime = 1
    if num == 1:
        return 0
    while primes[ix]<=sqrt(num):
        if num%primes[ix]== 0:
            prime = 0
            break
        ix+=1
    return prime

primes_reverse = []
cur_num = 19
#since there are only 11 primes that fit this criteria, we only continue until there are 11 values
while len(primes_reverse)<11:
    #only proceed to check the values if the first value is a prime
    if check_prime(cur_num):
        str_num_l = str(cur_num)
        is_prime = 1
        #if the value is prime, then check the string beginning to truncate from the left
        while len(str_num_l)>1:
            str_num_l = str_num_l[1:]
            if check_prime(int(str_num_l))==0:
                is_prime = 0
                break
            continue
        #if the value passes this first test then now remove strings from the right on
        str_num_r = str(cur_num)
        while len(str_num_r)>1 and is_prime == 1:
            str_num_r = str_num_r[:-1]
            if check_prime(int(str_num_r))==0:
                is_prime = 0
                break
            continue
        if is_prime == 1:
            primes_reverse.append(cur_num)
    #increment another number
    cur_num+=1
    #print cur_num
print sum(primes_reverse)
