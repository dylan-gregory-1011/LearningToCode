#import csv
#from binomial_reps import int_wrapper
import math
#primes  =[]

#using primes to find divisors we use n = a^x*b^y*c*z
#once we have found all the factors of these terms, we can use
#(x+1)*(y+1)*(z+1)... etc
#iterate through the list of traingles.  start with 1 and grow the increment value
#by 1 for each iteration
def get_Triangle():
    i = 2
    triangle = 1
    while 1:
        triangle+=i
        #for each triangle number, apply the divisors function
        if divisors(triangle)>500:
            print triangle
            break
        i+=1
#for the divisor function, iterate through all values between 2 and
#the square root of n.  for each divisor you find increment the divisor
#count by 2.  This is because for each value there are two divisors that
#we find.  Could have used the prime iteration of dividing by a first prime
#and incrementing through.
def divisors(number):
    divisors = 2
    n =2
    sq = math.sqrt(number)
    while n<=sq:
        if number%n == 0:
            divisors+=2
        n+=1
    return divisors

get_Triangle()
