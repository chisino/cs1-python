print("This program displays various information for a paint job\n")

sqFt = float(input("Enter the square feet of wall space to be painted: "))

paintPrice = float(input("Enter the price of paint per gallon: "))


# For every 112 sq feet, 1 gal of paint and 8 hours of labor are required

# 35$ per hour for labor

if (sqFt % 112 == 0):
    paintGal = sqFt / 112
else:
    paintGal = (sqFt / 112) + 1

hours = paintGal * 8

paintCost = paintGal * paintPrice

laborCharge = hours * 35

totalCost = laborCharge + paintCost

print("\nThe number of gallons of paint required is", format(paintGal, '.2f'))

print("The number of hours of labor required is", format(hours, '.2f'))

print("The cost of the paint is $", format(paintCost, '.2f'))

print("The labor charge is $", format(paintGal, '.2f'))

print("The total cost of the paint job is $", format(totalCost, '.2f'))
