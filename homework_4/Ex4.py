print("enter a year:")

year = int(input())

if year < 100_000_000 and year < 1800:
    print("incorrect data")
elif year % 4 == 0 and year % 400 == 0:
    print(year, "is leap year")
else:
    print(year, "is not leap year")
