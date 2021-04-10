print("This program determines the discount (if any) and total cost after the discount")

quantity = int(input("\nEnter the number of packages purchased: "))

fullCost = float(quantity * 99)

if (quantity < 10):
    print("\nNo discount")
    print("The price is $99")
elif (10 <= quantity <= 19):
    discount = fullCost * .1
    total = fullCost - discount
    print("\nThe discount is $",format(discount, '.2f'))
    print("The total amount is $",format(total, '.2f'))
elif (20 <= quantity <= 49):
    discount = fullCost * .2
    total = fullCost - discount
    print("\nThe discount is $",format(discount, '.2f'))
    print("The total amount is $",format(total, '.2f'))
elif (50 <= quantity <= 99):
    discount = fullCost * .3
    total = fullCost - discount
    print("\nThe discount is $",format(discount, '.2f'))
    print("The total amount is $",format(total, '.2f'))
elif (100 <= quantity):
    discount = fullCost * .4
    total = fullCost - discount
    print("\nThe discount is $",format(discount, '.2f'))
    print("The total amount is $",format(total, '.2f'))
