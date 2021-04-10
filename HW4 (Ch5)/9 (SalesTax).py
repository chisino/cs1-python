print("This program calculates sales tax\n")

monthSales = float(input("Enter the total sales for the month: "))

countyTax = monthSales * .025

stateTax = monthSales * .05

totalTax = countyTax + stateTax

print("\nThe county sales tax is $", format(countyTax, '.2f'))

print("The state sales tax is $", format(stateTax, '.2f'))

print("The total sales tax is $", format(totalTax, '.2f'))
