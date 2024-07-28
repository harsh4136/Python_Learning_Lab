# A year is a Leap year if it is divisible by 4, unless it is a century year that is not divisible by 400 (1800 and 1900 are
# not leap years, 1600 and 2000 are leap years). Write aprogram that calculates whether a given year is a leap year or not.

Year = int(input("Enter the year you want to find wheather it is leap year of not : "))

if (Year % 400 != 0) :
    print("You have entered century.")
elif (Year % 4 == 0) :
    print(f"{Year} is an leap year .")
else :
    print("You have entered incorrect data ! Please try again.")