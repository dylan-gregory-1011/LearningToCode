import os
import csv

os.chdir('C:\Users\dylan smith\Documents\Python\Intermediate_Python')
from binomial_reps import int_wrapper
primes  =[]
with open('primes.csv') as prime_list:
      reader = csv.reader(prime_list)
      reader = int_wrapper(reader)
      for row in reader:
          primes.append(row[0])
pandig = '987654321'
numbers = ['1','2','3','4','5','6','7','8','9']
#this gets all pandigital iterations from a previous set of iterations
def get_iterations(next_num, array_prev):
    array_iterate = 0
    new_array = []
    while array_iterate < len(array_prev):
        #begin
        new_array.append(next_num + array_prev[array_iterate])
        string_iterate = 1
        #place value in middle of string
        while string_iterate<len(array_prev[array_iterate]):
            new_array.append(array_prev[array_iterate][:string_iterate]+ next_num + array_prev[array_iterate][string_iterate:])
            string_iterate+=1
        #end of string
        new_array.append(array_prev[array_iterate] + next_num)
        array_iterate+=1

    return new_array
#three_array = get_iterations('3', ['12', '21'])
#four_array =  get_iterations('4', three_array)
#print len(four_array)
def see_if_prime(num, primes):
    index_primes = 0
    prime = 'Y'
    while index_primes<len(primes):
        if num%primes[index_primes] == 0:
            prime = 'N'
            break
        index_primes+=1
    return prime
print see_if_prime(15485863, primes)
len_array = 2
num_array = ['12', '21']
num_position = 2
prime_array = []
while len_array<9:
    new_pandig = pandig[:-len_array]
    array_iterate = 0
    while array_iterate<len(num_array):
        calc_num=  new_pandig + num_array[array_iterate]
        int_val = int(calc_num)
        int_val_array = int(num_array[array_iterate])
        prime_val = see_if_prime(int_val, primes)
        prime_array_val = see_if_prime(int_val_array, primes)
        if prime_val == 'Y':
            print calc_num
        if prime_array_val == 'Y':
            prime_array.append(int_val_array)
        array_iterate+=1
    if prime_val == 'Y':
        break
    num_array = get_iterations(numbers[num_position], num_array)
    num_position+=1
    print num_position
prime_array.sort()
print prime_array
