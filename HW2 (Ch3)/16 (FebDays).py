print("This program determines if the year entered is a leap year")

year = int(input("\nEnter a year: "))

if ( (year % 100 == 0) and (year % 400 == 0) ):
    print("\nIn",year,"February has 29 days.")
elif ( (year % 100 != 0) and (year % 4 == 0) ):
    print("\nIn",year,"February has 29 days.")
else:
    print("\nIn",year,"February has 28 days.")




    
