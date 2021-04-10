print("This program reads a file's contents and displays information about it")

def main():
    try:

        file = open('text.txt', 'r')

        text = file.read()

        countUp = 0
        countLow = 0
        countDig = 0
        countWht = 0

        for i in text:
            if i.isupper():
                countUp += 1
            elif i.islower():
                countLow += 1
            elif i.isdigit():
                countDig += 1
            elif i.isspace():
                countWht += 1
        
        print()
        print(countUp,'uppercase letters in the file',)
        print(countLow,'lowercase letters in the file',)
        print(countDig,'digits in the file',)
        print(countWht,'white spaces in the file',)

        file.close()

    except(IOError):
        print("File must be valid")
        

main()
