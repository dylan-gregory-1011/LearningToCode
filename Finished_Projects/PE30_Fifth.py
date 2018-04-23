i = 0
#create an empty dictionary to store all the values and their fifth power equivalent
fifths = {}
#use the i value to add all values between 0 and 9
while i<10:
    fifths[str(i)]= i**5
    i+=1
n = 20
#we only need to go up to the max value times 6 because any more then this would not be possible to add the fifths to get the value
ultimate_max = fifths['9']*6
final_array = []
#work our way through the integers between 1 and the max value.  Can limit this based on logic but didnt need to.
while n < ultimate_max:
    str_n = str(n)
    num_sum = 0
    #apply the fifths value to each number in the total number and add them up to get the total
    for num in str_n:
        num_sum += fifths[num]
    #if the numbers match then add it to the array.  If not go to the next one
    if num_sum == n:
        final_array.append(int(str_n))
    n+=1

print final_array
print sum(final_array)
