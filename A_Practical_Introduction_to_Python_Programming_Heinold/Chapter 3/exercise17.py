
"""
17. A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years
unless they are also divisible by 400. Ask the user to enter a year, and, using the // operator,
determine how many leap years there have been between 1600 and that year.
"""

year = 1992
for i in range(1600,year):
    leap_year = year % 4
    if (year  100) == 0 and (year // 400) == 0:
        print("this year is leap year")
    else:
        print("this is not")
"""    
    for i in range(1600,year):
        if lea
        """