from assorted_Math import proper_divisors
#create an original count of 0 and increment once we find a new one
amicable_count = 0
amicable = []
integer = 2
#make our way through all integers and check if the value is an amicable number
while integer<=10000:
    if integer in amicable:
        integer+=1
        continue
    #find an array of the divisors and get the sum of all these divisors
    #the proper divisors function creates an array of the values of divisors by iterating through all integers less then the
    #sqrt of the number and adding the divisors where n%i==0.
    divisors = proper_divisors(integer)
    sum_div = sum(divisors)
    if sum_div == 1:
        integer +=1
        continue
    if sum_div==integer:
        integer+=1
        continue
    #once we have the sum of the current integers values, we applied the same process as above and see if the new sum of
    #divisors is equal to the original integer.
    new_divisors = proper_divisors(sum_div)
    sum_div_new = sum(new_divisors)
    if integer == sum_div_new:
        amicable.append(integer)
        amicable_count+=1
        print integer
    integer+=1
print sum(amicable)
