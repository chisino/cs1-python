price1 = float(input("Enter the price of the first item: "))

price2 = float(input("Enter the price of the second item: "))

price3 = float(input("Enter the price of the third item: "))

price4 = float(input("Enter the price of the fourth item: "))

price5 = float(input("Enter the price of the fifth item: "))

subTotal = price1 + price2 + price3 + price4 + price5

salesTax = subTotal * .07

total = subTotal + salesTax

print("\nSubtotal: $", format(subTotal, '.2f'))

print("Sales Tax: $", format(salesTax, '.2f'))

print("Total: $", format(total, '.2f'))
