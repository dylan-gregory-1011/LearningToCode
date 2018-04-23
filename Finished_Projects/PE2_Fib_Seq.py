from zeckendorf_Rep import find_fib

fib_seq = find_fib(4000000)

#with the fib seq we are trying to find the fibinaci sequence with the first 4 million terms
#once we have the array of the fibincaci sequence we sum all the values of every third term
print fib_seq
i =1
sum_fib = 0
while i<len(fib_seq):
    sum_fib+=fib_seq[i]
    i+=3

print sum_fib
