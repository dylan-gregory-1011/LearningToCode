"""
Returns the breakdown of coins for a specified amount given.  Great for those people who are terrible at
counting
"""

import math
import random

strChange = input("How much change do you have?")

change = float(strChange)

while change !=0:
    change_Left= change
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0

    if(change_Left>0.25):
        quarters = change_Left//0.25
        change_Left = change_Left - quarters*0.25

        print "you will receive %i quarters" %(quarters)

    if(change_Left>0.1):
        dimes = change_Left//0.1
        change_Left = change_Left - dimes*0.1

        print "you will receive %i dimes" % (dimes)

    if(change_Left > 0.05 ):
        nickels = change_Left//0.05
        change_Left -= nickels*0.05

    print "you will receive %i nickels" %(nickels)

    pennies = change_Left//0.01
    change_Left-= pennies*0.01

    print 'You will receive %i pennies' %(pennies)

    if(change_Left!=0):
        print "yall done fucked up"
        print change_Left

    #strChange = input("How much change do you have?")
    #strChange = '0.00'
    #change = float(strChange)
