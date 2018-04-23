def power_Sums(max_num):
    #initiate the power_sum array
    power_Sum = [1]
    i = 2
    #while the factorial is less then 10 then iterate through this loop to calculate up to 9 Factorial
    while i< 10:
        j = 0
        carry = 0
        #reset the carry counter and index array
        while j<len(power_Sum):
            #calculate the new term by multiplying the previous value by the current number and making sure to add the carry value.
            power_Sum[j]= power_Sum[j]*i + carry
            #update the carry value for the next array value and set the current array value to the correct value. increment the index array once.
            carry = power_Sum[j]//10
            power_Sum[j] = power_Sum[j]%10
            j+=1
        #if the last value in the array and the carry value combine to be greater then 10.  Then append a new value and reset the carry values
        if power_Sum[j-1] + carry >= 10:
            power_Sum.append((power_Sum[j-1] + carry)%10)
            carry = (power_Sum[j-1] + carry)//10
        #once through the entire array then append the correct values on the end of the array.  Depending on the carry over we need to add more values on
        while carry>0:
            if carry > 10:
                power_Sum.append(carry%10)
                carry = carry//10
                continue
            if carry == 10:
                power_Sum.append(0)
                power_Sum.append(1)
                break
            if carry<10:
                power_Sum.append(carry)
                carry = 0
                break
        i+=1
    #for values greater then 10 and less than the the max number, we need to iterate through these values in a different fashion then the first time
    while i<=max_num and i>9:
        #break the current number into two values, one for each digit.
        str_I = str(i)
        str_1 = int(str_I[1])
        str_2 = int(str_I[0])
        j = 0
        carry = 0
        power_1 = []
        #set an initial array that will be the first digit's multiplication sum.  Iterate through the same way as the first method.  Append the new values
        #onto the new array (1) by multiplying the previous factorial solution value times the current integer and adding the carry over. Reset the carry and
        #increment on
        while j<len(power_Sum):
            power_1.append(power_Sum[j]*str_1 + carry)
            carry = power_1[j]//10
            power_1[j] = power_1[j]%10
            j+=1
        #once we are through the current previous' factorial solution then handle the carry values and carry on.
        while carry>0:
            if carry > 10:
                power_1.append(carry%10)
                carry = carry//10
                continue
            if carry == 10:
                power_1.append(0)
                power_1.append(1)
                break
            if carry<10:
                power_1.append(carry)
                carry = 0
                break
        j = 0
        carry = 0
        power_2 = [0]
        #this loop is for the second tens place value from the new number on the factorial and calculates a new array (starting with an array of 0) based on
        #the value of the current integer as well as the previous sequences' solution.
        while j<len(power_Sum):
            power_2.append(power_Sum[j]*str_2 + carry)
            carry = power_2[j+1]//10
            power_2[j+1] = power_2[j+1]%10
            j+=1
        while carry>0:
            if carry > 10:
                power_2.append(carry%10)
                carry = carry//10
                continue
            if carry == 10:
                power_2.append(0)
                power_2.append(1)
                break
            if carry<10:
                power_2.append(carry)
                carry = 0
                break
        carry = 0
        j = 0
        #we now have two arrays, one for each digit in the new factor.  We now must iterate over each of the values of both these arrays and sum both values as well
        #as any carry over.  This creates our new factorial solution moving forward.  We also must account for a difference in the lengths of the calculated arrays
        #and the correct terms to append on the end of the new solution array.
        while j < len(power_1):
            power_2[j] = power_2[j]+ power_1[j]+ carry
            carry = power_2[j]//10
            power_2[j] = power_2[j]%10
            j+=1
        while carry>0 and (len(power_2) - len(power_1) == 0):
            power_2.append(1)
            carry = 0
            break
        while carry>0 and (len(power_2) - len(power_1) !=0):
            power_2[j] = power_2[j]+ carry
            if power_2[j]>10:
                power_2[j] = power_2[j]%10
                power_2.append(power_2[j]//10)
            if power_2[j]==10:
                power_2[j] = 0
                try:
                    power_2[j+1] = power_2[j+1] +1
                except IndexError:
                    power_2.append(1)
            carry = 0
        #reset the solution array as the array we just calculated
        power_Sum = power_2
        i+=1
    i = 0
    sum_power = 0

    print power_Sum
    print sum(power_Sum)

power_Sums(99)
