import random

MIN = 0

MAX = 500

def main():
    print("This program will give two random numbers to be added and determines if the answer is correct\n")

    randomNum()


def randomNum():
    num1 = random.randint(MIN,MAX)
    num2 = random.randint(MIN,MAX)

    print(num1)
    print("+")
    print(num2)

    answer = int(input("Enter the answer: "))

    if (answer == num1 + num2):
        print("\nCongratulations, you are correct!")
    else:
        print("\nIncorrect, the correct answer is",num1+num2)
    
main()
