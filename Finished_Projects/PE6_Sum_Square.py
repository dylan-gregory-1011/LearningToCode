i = 1
sum_sum = 0
#get the sum of all values between 1 and 100
while i<=100:
    sum_sum+=i
    i+=1

#get the squared values of each number between 1 and 100 
i = 1
sq = 0
while i<=100:
    sq += i**2
    i+=1
print sum_sum**2-sq
