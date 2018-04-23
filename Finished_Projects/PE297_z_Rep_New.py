from datetime import datetime
from assorted_Math import find_fib

max_num = 10**17
#get the fibinacci sequence for all numbers up to and one greater then the max number.  Also initialize the index position
#to be iterated over
fib_seq =  find_fib(max_num)
fib_ix = 0
#set the first number and initialize the sum
n = 2
count =3

#create an array to record all the sums of the differences between the fibinaci numbers.  Make sure there is a
#value of 1 in the second value.  Also specify the current fibinacci index and maintain this throughout the problem
s_arr = [1,2]
s_arr[1] = 1
c_ix = 1

#initialize the two previous "sums" that were beweteen the initial fibinacci sequences
sum_1 = 2
prev = 1

#create an array which we will add to the previous sums to allow to add the correct sum.
#change the second value to be zero to match the pattern and intialize the index
f_add = fib_seq[:]
f_add[1] = 0
f_add_ix = 0



#initialize the new_sum to be calculated for the next batch of numbers
new_sum = 0
while n<max_num:
    #add to the count to capture the previous sum
    count+=new_sum
    #calculate the new sum between the fibinacci numbers to be used in two rounds.  This uses the current fibinacci number and the two previous sum of the arrays
    new_sum = prev + sum_1 +f_add[f_add_ix]
    #move the place holder over to capture the current sum of the array between the current fib number and the two previous
    prev = sum_1
    sum_1 = new_sum
    #reset the fibinacci index as well as increment the integer that declares the sum of all previous numbers
    #by the last fibinacci number
    fib_ix+=1
    n+=fib_seq[fib_ix]
    if n>max_num:
        #once we our current fibinacci is greater then the max number we need to reset the count and number
        count-=(prev +1)
        n -= fib_seq[fib_ix]
        #for the remainder of the iterations we need to calculate the difference between the current number and the max number
        #as well as reset the index
        f_add_ix = 0
        diff = max_num - n
        #ensure that the index is within the range
        try:
            fib_seq[c_ix]
        except IndexError:
            c_ix -=1
        #while the difference is not zero, iterate through and add to the sum
        while diff !=0:
            #ensure that we add a fibinacci sum that is less then the difference between the number and the max number.
            #if the current index is on a number greater then the difference, iterate through until it is less
            while (diff < fib_seq[c_ix]):
                c_ix -=1
            #update the difference and the sum.  THe difference we simply subtract the fibinacci number but the
            #count we need to add the current sum array with the fibinacci sequence multiplied by the amount of times we have iterated through to find the difference
            #this captures how many the addition of sub-arrays and their correct factors.
            #everytime we find a fibinacci number we need to add one to the factor multiplier
            count+=(s_arr[c_ix]+fib_seq[c_ix]*f_add_ix)
            diff-=fib_seq[c_ix]
            f_add_ix+=1
        break
    #this section ensures that we append all valid fib array sums as well as increment the indexs
    s_arr.append(new_sum)
    c_ix +=1
    f_add_ix+=1

print count
