def power_2(max_num):
    #start at 1 since 2^0 is one.  Work all the way to the max value.
    power_2 = [1]
    i = 0
    while i<max_num:
        #for each new number start the process at the beginning of the array and have no carry over
        j = 0
        carry_over = 'N'
        while j<len(power_2):
            #calculate the new value in the first position.
            power_2[j]= power_2[j]*2
            #if there is a carry over from the previous spot in the array then add one to the calculated value and reset the carry over
            if carry_over == 'Y':
                power_2[j]+=1
                carry_over = 'N'
            #if the new calculated value is greater then 10 then subtract 10 from the value and apply the carry over logic for the next iteration
            if power_2[j]>=10:
                power_2[j] -=10
                carry_over = 'Y'
            j+=1
        #if the last value in the array is 10 then handle this logic and move on to the next power of two..
        if power_2[j-1]==10:
            power_2[j-1]=0
            power_2.append(1)
        if carry_over == 'Y':
            power_2.append(1)
        i+=1
    print power_2

    print sum(power_2)
power_2(1000)
