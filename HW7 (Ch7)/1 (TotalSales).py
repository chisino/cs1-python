print("This program displays the total sales for a week")

def main():

    try:
        mon = float(input("\nEnter the sales for Monday: "))
        tues = float(input("\nEnter the sales for Tuesday: "))
        wed = float(input("\nEnter the sales for Wednesday: "))
        thurs = float(input("\nEnter the sales for Thursday: "))
        fri = float(input("\nEnter the sales for Friday: "))
        sat = float(input("\nEnter the sales for Saturday: "))
        sun = float(input("\nEnter the sales for Sunday: "))

        weekSales = []

        weekSales.append(mon)
        weekSales.append(tues)
        weekSales.append(wed)
        weekSales.append(thurs)
        weekSales.append(fri)
        weekSales.append(sat)
        weekSales.append(sun)

        total = 0.0

        for i in range(0, len(weekSales)):
            total = total + weekSales[i]

        print("\nThe total sales for the week is $", format(total, '.2f'))

    except ValueError:
        print("Entered sales values must be valid numbers")


main()
