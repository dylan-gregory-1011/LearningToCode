
def collatz(highest_num):
    i = 13
    max_iter = 0
    max_num = 0
    #begin at 13 and then iterate through all values below 1 million
    #increment the iteration number every time the value does not equal one.
    while i<=highest_num:
        number = i
        iter_over = 1
        while number!=1:
            iter_over+=1
            #if the number is even then reset number at n/2 and continue
            if number%2==0:
                number = number/2
            #if the number is odd then reset the number and continue
            else:
                number = 3*number +1
        #if the iteration amount is greater then the current max then reset the
        #current max
        if iter_over>max_iter:
            max_iter = iter_over
            max_num = i
        i+=1
    print max_iter
    print max_num

collatz(1000000)
