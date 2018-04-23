"""
Checking if three values are pythagorean squares.  To be honest you should remember most values from your calculus
classes anyways. 
"""

import random
import math
import time


user_num1_Str = input("What is your first number?\n")
user_num1 = int(user_num1_Str)
user_num2_Str = input("What is your second number?\n")
user_num2 = int(user_num2_Str)
user_num3_Str = input("What is your third number?\n")
user_num3 = int(user_num3_Str)
print("\n Thinking... \n")
time.sleep(2)



def squared(num):
    square = num*num
    return square

sq_num1 = squared(user_num1)
sq_num2 = squared(user_num2)
sq_num3 = squared(user_num3)

if (sq_num1+sq_num2==sq_num3) or (sq_num2+sq_num3==sq_num1) or (sq_num3+sq_num1==sq_num2) :
    print "Your values, %i, %i and %i are a pythagorean triple" % (user_num3,user_num2,user_num1)
else:
    print "Your values %i, %i and %i are not a pythagorean triple"% (user_num1,user_num2, user_num3)

'''
print "Number 1 is %i" % num1
print "Number 2 is %i" % num2
print "Number 1 and 2 squared is %i and %i respectively" %(sq_num1, sq_num2)
print "Number 3 is %i and this squared is %i" % (num3, sq_num3)
'''
