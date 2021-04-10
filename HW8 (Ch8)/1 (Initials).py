print("This program displays initials from a given name")

def main():
    try:
        name = input("\nEnter a first, middle, and last name: ")

        nameList = name.split()

        print(nameList[0][0] + '.' + ' ' + nameList[1][0] + '.' + ' ' + nameList[2][0] + '.')

    except(ValueError):
        print("Name must be a valid string with a first, middle, and last name")
        

main()
