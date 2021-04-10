print("This program displays data about a series of 20 numbers")
print()

def main():

    try:
        i = 0

        numList = []
    
        while i < 10:
           num = int(input("Enter a number: "))
       
           numList.append(num)

           i += 1

        total = 0

        for t in range(0, len(numList)):
            total = total + numList[t]

        numEle = len(numList)

        avg = total / numEle

        print("\nThe lowest number in the list is", min(numList))
        print("The highest number in the list is", max(numList))
        print("The total of the numbers in the list is", total)
        print("The average of the numbers in the list is", avg)

    except ValueError:
        print("Values entered must be valid numbers")


main()
