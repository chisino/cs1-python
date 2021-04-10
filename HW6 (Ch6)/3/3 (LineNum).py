def main():
    print("This program prints out lines from a file and numbers them\n")
    
    fileName = input("Enter the name of a file: ")

    in_file = open(fileName, 'r')

    contents = in_file.readline()

    print(1,':',contents) #printing the first line

    i = 2 #starting i at 2 (second line)

    for contents in in_file:
        print(i,':',contents)
        i += 1

    in_file.close()

main()
