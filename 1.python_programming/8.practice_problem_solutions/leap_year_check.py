'''
leap year : year has 366 days
condition 1 for century years ==> (year % 400 == 0) and (year % 100 == 0)
OR
condition 2 for non century years ==> (year % 4 == 0) and (year % 100 != 0)
'''

def check_leap_year(year):
    if (year % 400 == 0) and (year % 100 == 0):
        print(f"{year} is leap year")
    elif (year % 4 == 0) and (year % 100 != 0):
        print(f"{year} is leap year")
    else:
        print(f"{year} is not leap year")

check_leap_year(2004)