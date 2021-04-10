def main():
    print("This program reads numbers in a file and calculates their total\n")

    numFile = open("numbers.txt")

    contents = int(numFile.readline())

    total = contents

    for contents in numFile:
        total += int(contents)

    print("The sum of the numbers is", total)

    numFile.close()

main()
