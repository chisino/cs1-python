def main():
    print("This program counts the number of names in a file\n")

    names_file = open("names.txt","r")

    contents = names_file.readline()

    counter = 1

    for contents in names_file:
        counter +=1

    print("There are",counter,"names in this file")

    names_file.close()


main()
