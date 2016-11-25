#to finish with LEAP year requirement

#1. write stub daysInMonth(year, month) #always returns 30
#2. modify nextDay(year, month, day) to use daysInMonth(year, month)
#3. test nextDay(year, month, day) using stub daysInMonth
#4. modify daysInMonth(year, month) to be correct EXCEPT for leap years
#5. test nextDay again
#6. write isLeapYear(year) helper procedure
#7. test leapYear
#8. test all test cases
def isleapYear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False

print isleapYear(2013)



def daysInMonth(year, month):
    if month in (1, 3, 5, 7, 8, 10, 11):
        return 31
    else:
        if month == 2:
            if isleapYear(year):
                return 29
            else:
                return 28
    return 30

def nextDay(year, month, day):
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1

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

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

#testing#

def test():
    assert daysBetweenDates(2013, 1, 1, 2013, 1, 1) == 0
    assert daysBetweenDates(2013, 1, 1, 2013, 1, 2) == 1
    assert nextDay(2013, 1, 1) == (2013, 1, 2)
    assert nextDay(2013, 4, 30) == (2013, 5, 1)
    assert nextDay(2012, 12, 31) == (2013, 1, 1)
    assert nextDay (2013, 2, 28) == (2013, 3, 1)
    assert nextDay (2013, 9, 30) == (2013, 10, 1)
    assert nextDay (2012, 2, 28) == (2012, 2, 29)
    assert daysBetweenDates(2012, 2, 28, 2012, 2, 29) == 1
    assert daysBetweenDates(2012, 1, 1, 2013, 1, 1) == 366
    assert daysBetweenDates(2013, 1, 1, 2014, 1, 1) == 365

    print "test finished"
test()
