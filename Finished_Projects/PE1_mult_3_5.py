sum_val = 0
i = 0

#find the multiples of 3 from 3 to 1000
while i<1000:
    sum_val+=i
    i+=3

i = 5
sum_val+=i
#add to the previous array the multiples of 5 that arent also multiples of 3
#also sum the values
while i<995:
    i+=5
    sum_val+=i
    i+=10
    sum_val+=i

print sum_val
