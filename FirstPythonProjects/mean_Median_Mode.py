"""
Math terms, dont think to hard about it.  Looking back this is terrible code.  Please forgive
my 2016 self.  I had never done this before.
"""

import random

list_of_Numbers = [0]
i = 0
while i < 20:
    new_Num = random.randint(1,30)
    list_of_Numbers.append(new_Num)
    i +=1

def mean(list_of_Numbers):
    i = 0
    sum_LON = 0.00
    while i <20:
        sum_LON += list_of_Numbers[i]
        i+=1
    mean = sum_LON/i
    print " the mean is %.2f" % (mean)
    return mean

def median(list_of_Numbers):
    list_of_Numbers.sort()
    length_LON = len(list_of_Numbers)
    if(length_LON%2!=0):
        print "the median is %i" % (list_of_Numbers[length_LON//2])
        return list_of_Numbers[length_LON//2]
    else:
        med_Spot = length_LON//2
        med = (list_of_Numbers[med_Spot]+list_of_Numbers[med_Spot - 1])/2
        print "the median is %i" % (med)
        return med

def mode(list_of_Numbers):
    list_of_Numbers.sort()
    i = 0
    j = 0
    j_Max = 0
    k = list_of_Numbers[i]
    print list_of_Numbers
    while i< len(list_of_Numbers) - 1:
        i+=1
        if(k == list_of_Numbers[i]):
            j+=1
            if(j_Max < j ):
                j_Max = j
                mode = [list_of_Numbers[i]]
            elif(j_Max == j):
                mode.append(list_of_Numbers[i])
        else:
            k = list_of_Numbers[i]
            j = 0
    print "The mode is ", mode

mean(list_of_Numbers)
median(list_of_Numbers)
mode(list_of_Numbers)
