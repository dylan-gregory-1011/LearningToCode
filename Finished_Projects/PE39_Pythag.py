import math
#provide a function that returns only pythagorean integers else 0
def get_squared(a, b):
    c = math.sqrt(a**2+b**2)
    if c == int(c):
        return c
    else:
        return 0
print get_squared(3,5)
#create a dictionary that allows us to store the sum values and the
#amount of terms that fit it
pythagorean_sum = dict()
max_val = 1000
a = 2
#approximate a value where the sum would be less then 1000
while a*3 <=max_val:
    b= a+1
    #reset b as one more then a and approximate a new value that would
    #keep the sum less then  1000
    while a+2*b<=max_val:
        c = get_squared(a,b)
        if c!= 0:
            sum_len = a + b + c
            #check the dictionary.  If the sum is not a key, make a key,
            #else if it is a key, add one to the value.
            if sum_len in pythagorean_sum:
                pythagorean_sum[sum_len]+=1
            else:
                pythagorean_sum[sum_len]= 1
        b+=1
    a+=1

#print max([i for i in pythagorean_sum.values()])
print max(pythagorean_sum, key = pythagorean_sum.get)
