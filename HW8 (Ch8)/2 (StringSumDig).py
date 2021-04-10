print("This program takes a number and calculates the sum of the individual numbers")

def main():

    try:

        digits = input("\nEnter a number: ")

        sumDig = 0

        for i in range(0,len(digits)):
            sumDig += int(digits[i])
        
        print(sumDig)
        
    except(ValueError):
        print("Must be a valid number")

main()
