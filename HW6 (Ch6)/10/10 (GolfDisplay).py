def main():
    print("This program displays the records from golf.txt\n")

    golf_file = open("golf.txt","r")

    contents = golf_file.readline()

    print(contents)

    for contents in golf_file:
        print(contents)

    golf_file.close()

    
main()
