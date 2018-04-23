#create a dictionary that has the number of days per month
months_dict = {"Jan": 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May':31, "Jun": 30, 'Jul': 31, 'Aug':31, 'Sep':30, 'Oct':31, 'Nov':30, 'Dec':31}
#this array allows us to iterate over the months
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
year = 1901
Sunday = 6
first_Count = 0
#begin in 1901 where the first sunday was the sixth and iterate until the year is 2000
while year<2001:
    #begin with the month as 0 and iterate over all 12.
    mon = 0
    while mon<12:
        #if the month is Feburary, check to see if it is a leap year.  If not, increment the days by 7 and check to see if
        #it is the first day of the month.  if it is, increment the first sunday.  The first Feburary loop is to account for a
        #weird anomoly
        if months[mon] == 'Feb' and year%100==0 and year%400!=0:
            while Sunday <= 28:
                Sunday+=7
            Sunday-=28
            if Sunday == 1:
                first_Count+=1
            mon+=1
            continue
        #this Feburary loop accounts for leap years and incrementes the days by 7.  When it gets to be greater then 29 it subtracts 29 to check if the next
        #month is a friday. We continue at the end of this month to skip the typical process and increment the months by 1.
        if months[mon] == 'Feb' and year%4==0:
            while Sunday<=29:
                Sunday+=7
            Sunday -= 29
            if Sunday == 1:
                first_Count+=1
            mon+=1
            continue
        #for all other months follow the same process where we add the days by 7 until we have entered the next month and check to see if
        #the sunday of the next month is the first day of the month.
        while Sunday<=months_dict[months[mon]]:
            Sunday+=7
        Sunday -= months_dict[months[mon]]
        if Sunday == 1:
            first_Count+=1
        mon+=1
    year +=1

print first_Count
