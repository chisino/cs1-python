print("This program displays the assessment value and property tax\n")

propValue = float(input("Enter the actual value of the property: "))

assessValue = propValue * .6

if (assessValue % 100) == 0: 
    propTax = (assessValue / 100) * .72
else:
    propTax = ((assessValue / 100) + 1) * .72

print("\nThe assessment value is $", format(propValue, '.2f'))

print("The property tax is $", format(propTax, '.2f'))

