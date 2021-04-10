print("This program calculates the total cost of a meal purchased at a restaurant\n")

foodCharge = float(input("Enter the price of the food: "))

tip = foodCharge * .18

salesTax = foodCharge * .07

totalCost = foodCharge + tip + salesTax

print("\nThe charge is $", format(foodCharge, '.2f'))

print("The tip is $", format(tip, '.2f'))

print("The sales tax is $", format(salesTax, '.2f'))

print("The total is $", format(totalCost, '.2f'))
