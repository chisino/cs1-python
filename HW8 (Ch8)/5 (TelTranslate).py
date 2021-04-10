print("This program translates telephone numbers")

def main():

    try:

        tel = input("\nEnter a telephone number in the format XXX-XXX-XXXX: ")

        telNum = list(tel)

        for i in range(0,len(telNum)):
            if telNum[i] == 'A' or telNum[i] == 'B' or telNum[i] == 'C':
                telNum[i] = '2'
            elif telNum[i] == 'D' or telNum[i] == 'E' or telNum[i] == 'F':
                telNum[i] = '3'
            elif telNum[i] == 'G' or telNum[i] == 'H' or telNum[i] == 'I':
                telNum[i] = '4'
            elif telNum[i] == 'J' or telNum[i] == 'K' or telNum[i] == 'L':
                telNum[i] = '5'
            elif telNum[i] == 'M' or telNum[i] == 'N' or telNum[i] == 'O':
                telNum[i] = '6'
            elif telNum[i] == 'P' or telNum[i] == 'Q' or telNum[i] == 'R':
                telNum[i] = '7'
            elif telNum[i] == 'S' or telNum[i] == 'T' or telNum[i] == 'U':
                telNum[i] = '8'
            elif telNum[i] == 'V' or telNum[i] == 'W' or telNum[i] == 'X' or telNum[i] == 'Y' or telNum[i] == 'Z':
                telNum[i] = '9'

        for i in range(0, len(telNum)):
            print(telNum[i], end='')
        
    except(ValueError):
        print("Must be a valid number")

main()
