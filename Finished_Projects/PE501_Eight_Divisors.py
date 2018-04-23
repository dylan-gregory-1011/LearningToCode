divisor = 24
import math
#first while statement finds all the primes between 2 and the max number
#the second half finds the amount of eight divisors in the range

def find_primes(max_num):
    j = 24
    eight_divisor_found = 0
    primes = [2,3,5,7,11]
    sqrt_num = math.sqrt(max_num)

    while j<= max_num:
        i = 0
        number = j
        num = 1
        length = len(primes)
        while i<length and number!=1:
            if number%primes[i] == 0:
                number = number/primes[i]
            else:
                i+=1
        if int(number)==1:
            j+=1
            continue
        else:
            primes.append(int(number))
            primes.sort()
            j+=1
            continue

    print len(primes)
    total_divisors = 0
    i = 0
    j = 0
    k = 0
    length = len(primes)
    length_i = length - 1
    j_max = len(primes)
    k_max = len(primes)
    j_max_1 = len(primes)
    while i<length:
        j = i+1
        print i
        if math.pow(primes[i],7)<=max_num_pow:
            total_divisors +=1
        max_primes_1=max_num_pow/(primes[i]*primes[i]*primes[i])
        max_primes_2= (max_num_pow/primes[i])**(1/3.00000)
        for prime in primes:
            if prime<max_primes_1:
                continue
            j_max = primes.index(prime)-1
            break
        for prime in primes:
            if prime<max_primes_2:
                continue
            j_max_1 = primes.index(prime)-1
            break
        while j<length:
            k = j+1
            max_primes_3 = max_num_pow/(primes[i]*primes[j])
            for prime in primes:
                if prime<max_primes_3:
                    continue
                k_max = primes.index(prime) -1
                break
            if j<= j_max:
                total_divisors += 1
            if j<=j_max_1:
                total_divisors += 1
            while k<length:
                if k<=k_max:
                    total_divisors+=1
                    k+=1
                else:
                    break
            j+=1
        i+=1

    print total_divisors


find_primes(100)
