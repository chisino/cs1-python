print("This program finds the number of bugs collected using a while loop")

i = 0
totalBugs = 0

while (i < 5):
    bugs = int(input("\nEnter the number of bugs collected each day: "))
    totalBugs += bugs
    i += 1
    
print("\nThe total number of bugs collected is", totalBugs)

