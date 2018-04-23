"""
In case you are curious about finding the fibonacci sequence and don't have any internet and also
dont care about optimal code.
"""
seq_num =10
if(seq_num == 0):
    print "The 0th fib seq term is 0"
if(seq_num== 1):
    print "The 1st fib seq term is 1"
if (seq_num == 2):
    print "The 2nd fib seq term is 2"

if seq_num>2:
    fib_num_Prev = 1
    fib_num = 1
    i = 3
    while i <= seq_num:
        fib_num_Prev_Holder = fib_num
        fib_num = fib_num+ fib_num_Prev
        fib_num_Prev = fib_num_Prev_Holder
        i+=1
    print "The %i fib term is %i" %(i - 1, fib_num)
