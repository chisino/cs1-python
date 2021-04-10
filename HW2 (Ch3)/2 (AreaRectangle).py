print("This program compares the areas of 2 rectangles based on length and width")

lengthOne = float(input("\nEnter the length of rectangle 1: "))
widthOne = float(input("Enter the width of rectangle 1: "))
lengthTwo = float(input("\nEnter the length of rectangle 2: "))
widthTwo = float(input("Enter the width of rectangle 2: "))

areaOne = lengthOne * widthOne

areaTwo = lengthTwo * widthTwo

if (areaOne > areaTwo):
    print("\nRectangle 1 has the greater area")
elif (areaTwo > areaOne):
    print("\nRectangle 2 has the greater area")
else:
    print("\nThe areas are the same")
