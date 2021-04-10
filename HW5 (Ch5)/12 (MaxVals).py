
def main():
    print("This program determines which integer is greater than the other\n")

    int1 = int(input("Enter the first number: "))

    int2 = int(input("\nEnter the second number: "))

    max(int1,int2)


def max(int1,int2):
    
    if (int1 > int2):
        print("\nThe value that is greater is", int1)
    elif (int2 > int1):
        print("\nThe value that is greater is", int2)
    else:
        print("\nThe values are equal")


main()
