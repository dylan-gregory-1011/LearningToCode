import math
def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

wt_Quarter = 5.6714 #weight in grams
wt_Dime = 2.268 #weight in grams
wt_Nickel = 5.213 #weight in grams
wt_Penny = 2.50 #weight in grams


my_Quarters = 17
my_Dimes = 27
my_Nickels = 18
my_Pennys = 22
total_weight =0.000000
total_weight = wt_Quarter*my_Quarters + wt_Dime*my_Dimes + wt_Nickel*my_Nickels
round(total_weight, 6)
print "Total weight is %.4f" %(total_weight)
'''
quarter_Wrapper = 40
nickel_Wrapper = 40
dime_Wrapper = 50
penny_Wrapper = 50

qty_Quarters = my_Quarters / wt_Quarter
qty_Dimes = my_Dimes/ wt_Dime
qty_Nickels = my_Nickels/ wt_Nickel
qty_Pennys = my_Pennys/ wt_Penny

q_Wraps = (qty_Quarters//quarter_Wrapper) + 1
n_Wraps = (qty_Nickels//nickel_Wrapper) +1
d_Wraps = (qty_Dimes//dime_Wrapper) + 1
p_Wraps = (qty_Pennys//penny_Wrapper) + 1

print "The amout of Quarter wraps is %i" % (q_Wraps)
print "The amout of nickel wraps is %i" % (n_Wraps)
print "The amout of dime wraps is %i" % (d_Wraps)
print "The amout of penny wraps is %i" % (p_Wraps)
'''

def wt_calc(total_weight):
    quarters = 0
    dimes = 0
    nickels = 0
    if(total_weight%wt_Quarter == 0):
        quarters = total_weight/wt_Quarter
        money =  quarters * 0.25
        print "You have %i quarters and $%.2f dollars" % (quarters, money)
    elif(total_weight%wt_Dime == 0):
        dimes =  total_weight/wt_Dime
        money = dimes *0.1
        print "You have %i dimes and $%.2f dollars" % (dimes, money)
    elif(total_weight%wt_Nickel== 0):
        nickels = total_weight/wt_Nickel
        money = nickels*0.05
        print "You have %i nickles and $%.2f dollars" % (nickels, money)
    else:
        quarters= 1
        coin_weight = 0.000000
        coin_weight = quarters*wt_Quarter
        it_Broke = 0
        while (coin_weight<total_weight):
            #print "initial coin weight is %.2f and quarters is %i" %(coin_weight, quarters)
            while(total_weight > quarters*wt_Quarter+ nickels*wt_Nickel):
                #ensuring that the amount of quarters and nickels isnt more than the total weight, reiterating dimes
                dimes = 0
                nickels = nickels +1
                coin_weight = wt_Quarter*quarters+wt_Nickel*nickels
                #recalculating the weight of the quarters and nickels.  if it is less than the total weight, we iterate dimes
                #print "%i quarters, %i nickles, %.2f coin weight" % (quarters, nickels, coin_weight)
                while(coin_weight<total_weight):
                    dimes = dimes + 1
                    coin_weight = coin_weight + wt_Dime
                    round(coin_weight,6)
                    #print "%i quarters, %i nickles,%i dimes, %.8f coin weight, %.8f total weight" % (quarters, nickels,dimes, coin_weight, total_weight)
                    if(isclose(coin_weight, total_weight,rel_tol=1e-09, abs_tol=0.0)):
                        money = nickels*0.05 + quarters*0.25 + dimes*0.1
                        print "You have %i quarters, %i nickles, %i dimes and $%.2f dollars and the weight is %.3f" %(quarters, nickels, dimes, money, coin_weight)
                        found_it=1
                        break
            #print "the coin weight is %.3f" %(coin_weight)
            nickels = 0
            dimes = 0
            quarters= quarters +1
            coin_weight = quarters*wt_Quarter

        if(found_it==0):
            print "You have entered an incorrect weight"
        else:
            print "Youre pretty awesome"

wt_calc(total_weight)
