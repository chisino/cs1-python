print("This program determines whether the coins entered add up to a dollar")

penny = float(input("\nEnter the number of pennies: "))
nickel = float(input("Enter the number of nickels: "))
dime = float(input("Enter the number of dimes: "))
quarter = float(input("Enter the number of quarters: "))

pennyVal = penny * .01
nickelVal = nickel * .05
dimeVal = dime * .10
quarterVal = quarter * .25

totalVal = pennyVal + nickelVal + dimeVal + quarterVal

if (totalVal == 1.0):
    print("\nCongratulations! You have won the game")
elif (totalVal < 1.0):
    print("\nAmount entered is less than one dollar")
else:
    print("\nAmount entered is more than one dollar")


