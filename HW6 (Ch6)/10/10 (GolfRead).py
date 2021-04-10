def main():
    print("This program reads golf records and saves them to a new file\n")

    golf_file = open("golfrecords.txt","r")

    copy_file = open("golf.txt","w")

    contents = golf_file.readline()

    copy_file.write(contents)

    for contents in golf_file:
        copy_file.write(contents)

    golf_file.close()

    copy_file.close()

    print("The records have been saved to golf.txt")

    
main()
