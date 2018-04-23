#create an array that has the length of each of the words for the numbers 1-10
single_digits = [3,3,5,4,4,3,5,5,4]
#use the same logic for the length of all the numbers between ten and nineteen
teens = [3,6,6,8,8,7,7,9,8,8]
#calculate the length of the tens factor in front of each number
tens = [6,6,5,5,5,7,6,6]

s = 0
h = 0
sum_letters = 0
#iterate through all the values between 1 and 1000, break the components into hundreds first
while h<10:
    #starting with zero (hundreds addition of 0) and working to nine hundred add to the value for each number
    s = 0
    hundred_add = 0
    #for values then 100 we have no hundreds multiplier.  For values over 100 add to this value.
    if h>0:
        hundred_add = single_digits[h-1] + 10
        sum_letters += (single_digits[h-1]+7)
    #start with the values 0-10 and increment the count
    while s<len(single_digits):
        sum_letters+=(single_digits[s]+hundred_add)
        s+=1
    teen = 0
    #go through all the teen values
    while teen<len(teens):
        sum_letters+=(teens[teen]+hundred_add)
        teen+=1
    t = 0
    #increment through the rest of the values from x20-x99 and append these counts
    while t<len(tens):
        s = 0
        sum_letters+=(tens[t] + hundred_add)
        while s<len(single_digits):
            sum_letters+= (tens[t]+single_digits[s]+ hundred_add)
            s+=1
        t+=1
    h+=1
print sum_letters + 11
