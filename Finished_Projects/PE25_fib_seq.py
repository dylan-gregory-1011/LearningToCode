i = 1
max_number = 1
#create the max number where there are 1001 digits
while i<1000:
    max_number = max_number*10
    i+=1
print len(str(max_number))
#continue to create the fibinacci sequence until we get to a number that is greater then 1000 digits.  
def fib_index(max_number):
    fib_prev_1 = 1
    fib_curr = 2
    index =3
    while fib_curr< max_number:
        fib_holder_1 = fib_curr
        fib_curr = fib_curr + fib_prev_1
        fib_prev_1 = fib_holder_1
        index+=1
    print index

fib_index(max_number)
