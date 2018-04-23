import math
i = 4
abundant = []
#find all the abundant sums
while i<28123:
    sqrt = math.sqrt(i)
    divisors = [1]
    j = 2
    #create an array of divisors and be sure to only count the squared values once.
    while j<=sqrt:
        if i%j == 0:
            divisors.append(j)
            k = i/j
            if k!=j:
                divisors.append(k)
        j+=1
    sum_num = sum(divisors)
    #if the sum of all the divisors is greater then the number, it is an abundant sum
    if sum_num>i:
        abundant.append(i)
    i+=1
number= 1
abundant_sum = 0
non_abundant_sums = range(1,28213)
i = 0
#now iterate over all the abundatnt terms and find the sum of each possible iteration that is below 28123.  Remove this value if it
#is in the array and then continue on
while abundant[i]*2 <28123:
    j = i
    abundant_i = abundant[i]
    while abundant_i+abundant[j]<28123:
        if abundant_i+abundant[j] in non_abundant_sums:
            non_abundant_sums.remove(abundant_i+abundant[j])
        j+=1
    i+=1
    print i
print sum(non_abundant_sums)
while number<=28123:
    i = 0
    equals = 'N'
    while abundant[i]<number:
        i+=1
    i-=1
    try:
        abundant[i]
    except IndexError:
        i-=1
    while i>=0:
        j = i
        if abundant[i]+abundant[j]<number:
            break
        while abundant[i]+abundant[j]>number and j>=0:
            j-=1
        if abundant[i]+abundant[j]==number:
            equals = 'Y'
            break
        i-=1
    if equals =='N':
        abundant_sum +=number
    else:
        print number
    number+=1

print abundant_sum
