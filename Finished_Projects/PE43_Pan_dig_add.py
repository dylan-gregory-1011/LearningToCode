i = 2
list_array = ['1']
#get the pandigital numbers including 0-9
#we first start with an array that is of '1' and work our way out
while i<11:
    new_list_array = []
    if i == 10:
        i = '0'
    #for every number instead of 10 we will create an array of all the panditigal numbers, Working recursively from 1
    for pandigital in list_array:
        #for all values except 0 create an array with the appended at the very beginning and all the values get added to the end
        if i != '0':
            new_list_array.append(str(i)+pandigital)
        new_list_array.append(pandigital + str(i))
        j = 1
        #we then create array entries that add the number to all points in the middle of the arrays
        while j<len(pandigital):
            new_list_array.append(pandigital[:j]+str(i)+pandigital[j:])
            j+=1
    list_array = new_list_array
    if i == '0':
        break
    i+=1

primes = [2,3,5,7,11,13,17]
digits_fit = 0
#take the array of pandigital numbers and try the division algorithm.  If the first number is divisible by a prime, work your way down
#the prime list to see if they all are.  If the value makes it through then add the number to the sum
for num in list_array:
    i = 1
    found = 1
    while i<=7:
        new_number = int(num[i:i+3])
        if new_number%primes[i-1]!= 0:
            found = 0
            break
        i+=1
    if found ==1:
        digits_fit+=int(num)
print digits_fit
