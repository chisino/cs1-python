print("This program prints the day of the week based on the number given")

number = int(input("\nEnter a number in the range of 1 through 7: "))

if (number == 1):
    print("Monday")
elif (number == 2):
    print("Tuesday")
elif (number == 3):
    print("Wednesday")
elif (number == 4):
    print("Thursday")
elif (number == 5):
    print("Friday")
elif (number == 6):
    print("Saturday")
elif (number == 7):
    print("Sunday")
else:
    print("Error: number not in range of 1 through 7")
