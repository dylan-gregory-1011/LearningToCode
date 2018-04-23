from numpy import isclose
two_pound_count = 0
one_pound_count = 0
fifty_p_count = 0
twenty_p_count = 0
ten_p_count= 0
five_p_count = 0
two_p_count = 0
one_p_count = 0
count = 0
#call a function to calculate the amount given the total amount of coins that we have
def coin_count(two_pound_count, one_pound_count, fifty_p_count, twenty_p_count, ten_p_count, five_p_count, two_p_count, one_p_count):
    return two_pound_count*2 + one_pound_count*1 + fifty_p_count*0.5 + twenty_p_count*0.2 + ten_p_count*0.1 + five_p_count*0.05 + two_p_count*0.02 + one_p_count*0.01
#call a function to ensure that the value is close.
def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

#starting with the two pound count as zero we set all other values to zero and move into the loop
while two_pound_count<=1:
    one_pound_count = 0
    fifty_p_count = 0
    twenty_p_count = 0
    ten_p_count= 0
    five_p_count = 0
    two_p_count = 0
    one_p_count = 0
    #starting with the one pound count as zero we set all sub values to zero and move on.  When this increments by one we reset all the other counts to zero
    total_change_2 = two_pound_count*2
    while one_pound_count<=2 :
        fifty_p_count = 0
        twenty_p_count = 0
        ten_p_count= 0
        five_p_count = 0
        two_p_count = 0
        one_p_count = 0
        #following the same process, increment the value by 1 when the nested while loops are complete and reset all the values to zero.
        #also make sure that the while loop controls so that once we get to a sum that is greater then two pounds it breaks
        total_change_1 = total_change_2 + one_pound_count
        while fifty_p_count <=(4 - total_change_1)/0.5 + 1:
            twenty_p_count = 0
            ten_p_count= 0
            five_p_count = 0
            two_p_count = 0
            one_p_count = 0

            total_change_05 = total_change_1 + fifty_p_count*0.5
            while twenty_p_count<=(2- total_change_05)/0.2 + 1:
                ten_p_count= 0
                five_p_count = 0
                two_p_count = 0
                one_p_count = 0

                total_change_02 = total_change_05 + twenty_p_count*0.2
                while ten_p_count<=(2- total_change_02)/0.1 + 1:
                    five_p_count = 0
                    two_p_count = 0
                    one_p_count = 0

                    total_change_01 = total_change_02 + ten_p_count*0.1
                    while five_p_count<=(2-total_change_01)/0.05 + 1:
                        two_p_count = 0
                        one_p_count = 0

                        total_change_005 = total_change_01 + five_p_count*0.05
                        while two_p_count<=(2-total_change_005)/0.02 + 1:
                            one_p_count = 0

                            total_change_002 = total_change_005 + two_p_count*0.02
                            while one_p_count<=(2 - total_change_002)/0.01 + 1:
                                cash = coin_count(two_pound_count, one_pound_count, fifty_p_count, twenty_p_count, ten_p_count, five_p_count, two_p_count, one_p_count)
                                if isclose(cash, 2.00, rel_tol=1e-09, abs_tol=0.0):
                                    count +=1
                                one_p_count+=1
                            two_p_count+=1
                        five_p_count+=1
                    ten_p_count+=1
                twenty_p_count+=1
            fifty_p_count+=1
        one_pound_count+=1
    two_pound_count+=1


print count
