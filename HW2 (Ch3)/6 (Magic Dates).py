print("This program determines if the date given is 'magic' or not")

month = int(input("\nEnter the month in numeric form: "))

day = int(input("Enter the day: "))

year = int(input("Enter a 2 digit year: "))


if ((month * day) == year):
    print("\nThe date is magic")
else:
    print("\nThe date is not magic")
