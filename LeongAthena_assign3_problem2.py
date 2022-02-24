# KAPP_ASSIGNMENT03_PART2
"""
Athena Leong
Section 04 2/10/2022
Problem #2
"""

# ask for date input YYYYMMDD
date = int(input("Enter a date (YYYYMMDD): "))
# isolate DD --> % 100
day = date % 100
# isolate MM --> ( % 10000) // 100
month = (date % 10000) // 100
#isolate YYYY --> ( % 100000000) // 10000
year = (date % 100000000) // 10000


# verify if it is a leap year
if year % 4 != 0:
    print(year, "is NOT a leap year")
    leap = "not a leap year"
else:
    if year % 400 == 0:
        print(year, "is a leap year")
        leap = "is a leap year"
    elif year % 100 == 0:
        print(year, "is NOT a leap year")
        leap = "not a leap year"
    else:
        print(year, "is a leap year")
        leap = "is a leap year"
# create labels for the corresponding number of the day
if day == 1 or day == 21 or day == 31:
    label = str(day) + "st"
elif day == 2 or day == 22:
    label = str(day) + "nd"
elif day ==3 or day == 23:
    label = str(day) + "rd"
else:
    label = str(day) + "th"
# verify if month and day is valid
# assign months to numbers, if within a range it is valid
# if it isn't, then it is not a valid date nor is it a valid month if >12
if month == 1:
    mm = "January"
    if day <= 31 and day > 0:
        print(mm, label, year, "is a valid date")
        valid = "y"
    else:
        print("This is not a valid date in", year)
        valid = "n"
elif month == 2:
    mm = "February"
    if leap == "not a leap year":
        if day <= 28 and day > 0:
            print(mm, label, year, "is a valid date")
            valid = "y"
        else: print("This is not a valid date in", year)
        valid = "n"
    else:
        if day <= 29 and day > 0:
            print(mm, label, year, "is a valid date")
            valid = "y"
        else:
            print("This is not a valid date in", year)
            valid = "n"
elif month == 3:
    mm = "March"
    if day <= 31 and day > 0:
        print(mm, label, year, "is a valid date")
        valid = "y"
    else:
        print("This is not a valid date in", year)
        valid = "n"
elif month == 4:
    mm = "April"
    if day <= 30 and day > 0:
        print(mm, label, year, "is a valid date")
        valid = "y"
    else:
        print("This is not a valid date in", year)
        valid = "n"
elif month == 5:
    mm = "May"
    if day <= 31 and day > 0:
        print(mm, label, year, "is a valid date")
        valid = "y"
    else:
        print("This is not a valid date in", year)
        valid = "n"
elif month == 6:
    mm = "June"
    if day <= 30 and day > 0:
        print(mm, label, year, "is a valid date")
        valid = "y"
    else:
        print("This is not a valid date in", year)
        valid = "n"
elif month == 7:
    mm = "July"
    if day <= 31 and day > 0:
        print(mm, label, year, "is a valid date")
        valid = "y"
    else:
        print("This is not a valid date in", year)
        valid = "n"
elif month == 8:
    mm = "August"
    if day <= 31 and day > 0:
        print(mm, label, year, "is a valid date")
        valid = "y"
    else:
        print("This is not a valid date in", year)
        valid = "n"
elif month == 9:
    mm = "September"
    if day <= 30 and day > 0:
        print(mm, label, year, "is a valid date")
        valid = "y"
    else:
        print("This is not a valid date in", year)
        valid = "n"
elif month == 10:
    mm = "October"
    if day <= 31 and day > 0:
        print(mm, label, year, "is a valid date")
        valid = "y"
    else:
        print("This is not a valid date in", year)
        valid = "n"
elif month == 11:
    mm = "November"
    if day <= 30 and day > 0:
        print(mm, label, year, "is a valid date")
        valid = "y"
    else:
        print("This is not a valid date in", year)
        valid = "n"
elif month == 12:
    mm = "December"
    if day <= 31 and day > 0:
        print(mm, label, year, "is a valid date")
        valid = "y"
    else:
        print("This is not a valid date in", year)
        valid = "n"
else:
    print("This is not a valid date in", year)
    valid = "n"

# if it was a valid date, ask for a hemisphere
# if it is a certain month, it will be a certain season
# different for each hemisphere so have if and elif and else (for inputs that aren't n or s)
if valid == "y":
    hemi = str.upper(input("Which hemisphere are you located in? (N)orth or (S)outh? "))
    if hemi == "N":
        if month == 12 or month <= 2:
            print("The season on this date is WINTER")
        elif 5 >= month >= 2:
            print("The season on this date is SPRING")
        elif 6 <= month <= 8:
            print("The season on this date is FALL")
        elif 9 <= month <= 11:
            print("The season on this date is AUTUMN")
        else:
            pass
    elif hemi == "S":
        if month == 12 or month <= 2:
            print("The season on this date is SUMMER")
        elif 5 >= month >= 2:
            print("The season on this date is AUTUMN")
        elif 6 <= month <= 8:
            print("The season on this date is WINTER")
        elif 9 <= month <= 11:
            print("The season on this date is SPRING")
        else:
            pass
    else:
        print("Invalid entry, cannot determine season")
else:
    pass


