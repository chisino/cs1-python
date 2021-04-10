def main():
    print("This program reads random numbers from a file\n")

    numFile = open("randomfile.txt", "r")

    contents = int(numFile.readline())

    print(contents)

    print()

    total = contents

    counter = 1

    for contents in numFile:

        print(contents)
        
        total += int(contents)

        counter += 1

    print("The total of the numbers is",total)

    print("There are",counter,"numbers in this file")

    numFile.close()


main()
