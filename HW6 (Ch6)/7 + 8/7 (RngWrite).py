MIN = 1
MAX = 100

import random

def main():
    print("This program writes a series of random numbers to a file\n")

    amount = int(input("Enter how many random numbers the file should hold: "))

    rngFile = open("randomfile.txt","w")

    for count in range(1, amount + 1):

        rngFile.write(str(random.randint(MIN,MAX)) + "\n")

    rngFile.close()

    print("\nThe random numbers have been written to the file")

main()
