
def isLeapYear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                leapYear = True
            else:
                leapYear = False
        else:
            leapYear = True
    else:
        leapYear = False
    return leapYear

def getNumOfDaysInMonth(month):
    # print month

    if month in (1,3,5,7,8,10,12):
        TotalDaysInMonth = 31
    elif month == 02:
        if isLeapYear(year) == True:
            TotalDaysInMonth = 29
        else:
            TotalDaysInMonth = 28
    elif month in(4,6,9,11):
        TotalDaysInMonth = 30
    else:
        raise Exception ("The given month {0} is invalid".format(month))
    return TotalDaysInMonth

def nextDay(day, month, year):
    try:
        if day < getNumOfDaysInMonth(month):
            day += 1

        elif day == getNumOfDaysInMonth(month):

            if month != 12:
                day = 1
                month += 1

            else:
                day = 1
                month = 1
                year += 1

        else:
            raise Exception ("Given date {0} is invalid".format(day))

        print "Next day is {0}-{1}-{2}".format(day, month, year)

    except Exception as error:
        print error


Date_string = raw_input("Enter a Date in dd-mm-yyyy format: ")

day = int(Date_string.split("-")[0])
month = int(Date_string.split("-")[1])
year = int(Date_string.split("-")[2])


nextDay(day,month,year)