import math


def find_Divisors(max_num):
    n =10
    divisors_match = 'No'
    divisors_prev = 2
    pos_divisors = 1
    while n<max_num:
        i = 2
        divisors = 2
        sqr_rt = math.sqrt(n)
        while i<sqr_rt:
            if n%i == 0:
                divisors +=2
            i+=1
        if sqr_rt%i == 0:
            divisors +=1
        if divisors == divisors_prev:
            pos_divisors +=1
            n+=1
        else:
            divisors_prev = divisors
            n+=1
    print pos_divisors
