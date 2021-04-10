print("This program determines whether a pocket number is green, red, or black")

pocket = int(input("\nEnter a pocket number in the range of 0 through 36: "))

if (pocket == 0):
    print("\nThe pocket is green")
elif ( (1 <= pocket <= 10) or (19 <= pocket <= 28) ):
    if (pocket % 2 == 1):
        print("\nThe pocket is red")
    else:
        print("\nThe pocket is black")
elif ( (11 <= pocket <= 18) or (29 <= pocket <= 36) ):
    if (pocket % 2 == 1):
        print("\nThe pocket is black")
    else:
        print("\nThe pocket is red")
else:
    print("\nError: The number is outside the range of 1 through 36")
