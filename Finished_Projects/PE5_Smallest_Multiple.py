primes  = [2,3,5,7,11,13,17,19]

def smallest_Mutliple(primes, value):
    factors = [2,3]
    i = 4
    while i<=20:
        if i in primes:
            factors.append(i)
            i+=1
            continue
        found = 'N'
        k = 0
        while k<len(primes):
            j = k+1
            value = primes[k]
            while j<len(factors):
                if factors[j]*value>i and i%factors[j-1]==0:
                    index = primes.index(factors[j])
                    factors.append(primes[index-1])
                    factors.sort()
                    found = 'Y'
                    break
                elif factors[j]*value== i:
                    found = 'Y'
                    break
                elif factors[j]*value<i and i%(factors[j]*value)==0:
                    value = factors[j]*value
                    j+=1
                    continue
                j+=1
            if found == 'Y':
                break
            k+=1

        i+=1
    print factors
    i = 0
    value = 1
    while i<len(factors):
        value = value*factors[i]
        i+=1
    print value
    return value
#smallest_Mutliple(primes, 20)

i = 2
factors = primes[:]

while i<=20:
    if i in primes:
        i+=1
        continue
    num = i
    while num>1:
        if z in primes for num%x = 0 for x in primes
