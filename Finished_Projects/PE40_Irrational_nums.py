
number_list = '1'
num = 2
#create an string that holds all the values between 1 and 1 million together
while len(number_list)<1000000:
    number_list = number_list + str(num)
    num+=1

#initiate the first index value as well as the initial  multiplication sum
divisor = 1
mult = 1
#increment the multiplier by a factor of 10 every time and multiply the current
#product by the new factor based on the indexed value
while divisor <=1000000:
    mult = mult*int(number_list[divisor-1])
    divisor *=10

print mult
