#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#
#NOTE: PLEASE OPEN THE SOLAR SYSTEM OF YOU WANT TO RUN THE PROGRAM#
#/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\#

#####################################
# Day Calc                          #
# Harshil Parikh                    #
# ICS 3UI                           #
# Mr.Schattman                      #
# 22/04/15                          #
#####################################

#BEGIN

#IMPORTS
from math import *

#Finds days between 2 dates
def calculateDaysBetween(date1, date2):
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    #Isolating day, month and year for both dates
    day1 = int(date1[4:-6])
    month1 = months.index(date1[:3]) + 1
    year1 = int(date1[8:])

    day2 = int(date2[4:-6])
    month2 = months.index(date2[:3]) + 1
    year2 = int(date2[8:])

    #If month is Jan/Feb then add 12 months and subtract 1 year
    if month1 <= 2:
        month1 += 12
        year1 -= 1

    if month2 <= 2:
        month2 += 12
        year2 -= 1

    #Finding days for both dates
    days1 = 365*year1 + floor(year1/4) - floor(year1/100) + floor(year1/400) + day1 + floor((153*month1+8)/5)
    days2 = 365*year2 + floor(year2/4) - floor(year2/100) + floor(year2/400) + day2 + floor((153*month2+8)/5)

    #Returning their difference as days passed
    return str(days2 - days1)

#END
