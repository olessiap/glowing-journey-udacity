# Given your birthday and the current date, calculate your age
# in days. Compensate for leap days. Assume that the birthday
# and current date are correct dates (and no time travel).
# Simply put, if you were born 1 Jan 2012 and todays date is
# 2 Jan 2012 you are 1 day old.

##breaking down the problem ##

#PSEUDOCODE for daysBetweenDates (3)#
#
# days = 0
# while date1 is before date2: #<--dateIsBefore (2)
#     date1 = day after date1 #<-- nextDay (1)
#     days = days + 1
# return days


## 1. nextDay - find next day assuming month has 30 days##

def nextDay(year, month, day):
    if day < 30:
        return year, month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1

# print nextDay(2016, 10, 30)
# print nextDay(2016, 12, 06)
# print nextDay(2015, 12, 30)

## 2.  helper procedure##
def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """returns True if year1-month1-day1 is before
        year2-month2-day2. otherwise, returns False"""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

print dateIsBefore(2016, 10, 06, 2016, 10, 07) # True
print dateIsBefore(2016, 10, 06, 2016, 11, 06) # True
print dateIsBefore(2018, 10, 06, 2017, 10, 06) # False

## 3. daysBetweenDates - approximate answers using the above nextDay procedure ###

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

print daysBetweenDates(2016, 10, 06, 2016, 10, 07) #>>1
print daysBetweenDates(2016, 10, 06, 2016, 11, 06) #>>30
print daysBetweenDates(2016, 10, 06, 2017, 10, 06) #>>360
print daysBetweenDates(2013, 1, 24, 2013, 6, 29) #>>155
print daysBetweenDates(2015, 1, 24, 2013, 6, 29) #>> 0
