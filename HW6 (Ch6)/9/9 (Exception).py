def main():
    print("This program reads numbers in a file and calculates their average\n")

    try:
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

    except IOError:
        print("An error occurred trying to read the file 'numbers.txt'")

    except ValueError:
        print("Error: Numbers in the file must be valid integers")
        

main()
