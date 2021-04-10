def main():
    print("This program reads numbers in a file and calculates their average\n")

    numFile = open("numbers.txt", "r")

    contents = int(numFile.readline())

    total = contents

    counter = 1

    for contents in numFile:
        total += int(contents)

        counter += 1

    avg = total / counter

    print("The average of the numbers is",avg)

    numFile.close()


main()
