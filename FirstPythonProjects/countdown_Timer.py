"""
Gives the correct difference between two date-time values.  Can't wait until the next olympics?
Give it a whirl.
"""

import datetime
import time
import sys

from time import localtime, strftime, sleep

months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', "nov", 'dec']
months_days = [31,28,31,30,31,30,31,31,30,31,30,31]

print strftime(" %b", localtime())
print "What date would you like the countdown for?(If today, enter today)"
date_Desire = raw_input("Enter date as MMM DD, YYYY")

print "Okay, now what time on that day?(In Military Time)"
time_Desire = raw_input("Enter time as HH:MM:SS")


def date_calc(date_Desire):
    month = date_Desire[:3].lower()
    date = int(date_Desire[4:6])
    year = int(date_Desire[-4:])
    mon_py=0
    if month in months:
        mon_index = months.index(month)
        mon_py = months.index(month) +1

    if date> months_days[mon_index]:
        print "Invalid date, please enter a new date"
        print "What date would you like the countdown for?(If today, enter today)"
        #date_Desire = raw_input("Enter date as MMM DD, YYYY")
        print "Okay, now what time on that day?"
        #time_Desire = raw_input("Enter time as HH:MM:SS")
        date_calc(date_Desire)
    return year, month, date

def time_calc(time_Desire):
    hour = int(time_Desire[:2])
    minute = int(time_Desire[3:5])
    second = int(time_Desire[6:8])
    return hour, minute, second

def date_diff(month, date, cur_month, cur_date):

    if month in months:
        mon_index = months.index(month)
    if month in months:
        cur_mon_index = months.index(cur_month.lower())
    i=0
    j = 0
    days_year_target = 0
    days_year_current = 0
    while (i<(mon_index - 1)):
        days_year_target+= months_days[i]
        i+=1
    while (j<(cur_mon_index - 1)):
        days_year_current+= months_days[j]
        j+=1
    days_year_current+=cur_date
    days_year_target += date
    dif_date = days_year_target- days_year_current - 1
    return dif_date

def date_Delta(date_Desire, time_Desire):
    hour, minute, second = time_calc(time_Desire)
    year, month, date = date_calc(date_Desire)
    hour_dif = 0
    min_dif = 0
    sec_dif = 0

    try:
        cur_month = strftime("%b", localtime())
        cur_year = int(strftime("%Y", localtime()))
        cur_date = int(strftime("%d", localtime()))
        count_down_Timer = True
        days_dif = date_diff(month, date, cur_month, cur_date)
        if (days_dif<0):
            raise ValueError("Target date already happened!")

        cur_hour = int(strftime("%H", localtime()))+12
        if(cur_hour>=24):
            cur_hour -=12
        cur_min = int(strftime("%M", localtime()))
        cur_sec = int(strftime("%S", localtime()))


        if(cur_hour- hour < 0):
            hour_dif = hour - cur_hour
            days_dif +=1
            if(cur_min- minute < 0):
                min_dif = minute - cur_min
                if(cur_sec- second < 0):
                    sec_dif = second - cur_sec
                if(cur_sec - second >0):
                    sec_dif = 60 - cur_sec + second
                else:
                    sec_dif= 0
            if(cur_min - minute >0):
                min_dif = 60 - cur_min + minute
                hour_dif -=1
                if(cur_sec- second < 0):
                    sec_dif = second - cur_sec
                if(cur_sec - second >0):
                    sec_dif = 60 - cur_sec + second
                else:
                    sec_dif= 0
            if(cur_min==minute):
                min_dif = 0
                if(cur_sec- second < 0):
                    sec_dif = second - cur_sec
                    days_dif +=1
                if(cur_sec - second >0):
                    sec_dif = 60 - cur_sec + second
                else:
                    sec_dif= 0
        if(cur_hour - hour >0):
            hour_dif = 24 - cur_hour + hour
            if(cur_min- minute < 0):
                min_dif = minute - cur_min
                if(cur_sec- second < 0):
                    sec_dif = second - cur_sec
                if(cur_sec - second >0):
                    sec_dif = 60 - cur_sec + second
                else:
                    sec_dif= 0
            if(cur_min - minute >0):
                min_dif = 60 - cur_min + minute
                if(cur_sec- second < 0):
                    sec_dif = second - cur_sec
                if(cur_sec - second >0):
                    sec_dif = 60 - cur_sec + second
                else:
                    sec_dif= 0
            if(cur_min==minute):
                min_dif = 0
                if(cur_sec- second < 0):
                    sec_dif = second - cur_sec
                if(cur_sec - second >0):
                    sec_dif = 60 - cur_sec + second
                else:
                    sec_dif= 0
        if(cur_hour==hour):
            if(cur_min- minute < 0):
                hour_dif = 0
                min_dif = minute - cur_min
                days_dif +=1
                if(cur_sec- second < 0):
                    sec_dif = second - cur_sec
                if(cur_sec - second >0):
                    sec_dif = 60 - cur_sec + second
                else:
                    sec_dif= 0
            if(cur_min - minute >0):
                min_dif = 60 - cur_min + minute
                hour_dif = 23
                if(cur_sec- second < 0):
                    sec_dif = second - cur_sec
                if(cur_sec - second >0):
                    sec_dif = 60 - cur_sec + second
                else:
                    sec_dif= 0
            if(cur_min==minute):
                min_dif = 0
                if(cur_sec- second < 0):
                    sec_dif = second - cur_sec
                if(cur_sec - second >0):
                    sec_dif = 60 - cur_sec + second
                else:
                    sec_dif= 0
                    days_dif +=1
                time.sleep(1)
                print "There is %i days, %i hours, %i minutes and %i seconds left in the countdown" % (days_dif, hour_dif, min_dif, sec_dif),

        while(days_dif>=0):
            while (hour_dif>=0):
                while (min_dif>= 0):
                    while(sec_dif>=0):
                        time.sleep(1)
                        print "\r"+"There is %i days, %i hours, %i minutes and %i seconds left in the countdown" % (days_dif, hour_dif, min_dif, sec_dif)
                        sec_dif-=1
                    min_dif-=1
                    sec_dif=59
                hour_dif -=1
                min_dif = 59
            days_dif-=1
            hour_dif = 23
        if(days_dif==0 and sec_dif == 0 and hour_dif == 0 and min_dif == 0):
            print "The timer has ended!!!!!"

    except KeyboardInterrupt:
            print "You have ended the timer"
    except ValueError:
        print "You have entered an invalid date"

date_Delta(date_Desire, time_Desire)
