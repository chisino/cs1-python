import random

MIN = 0

MAX = 100

def main():
    print("This program is a random number guessing game using numbers 0 to 100\n")

    again = 'y'

    while (again != 'n'):

        number = random.randint(MIN,MAX)

        guessing(number)

        again = input("\nEnter n to stop, anything else to play again: ")


def guessing(number):

    guess = int(input("\nEnter your guess: "))

    while (guess != number):
        if (guess > number):
            print("Too high, try again")

            guess = int(input("Enter your guess: "))
        elif (guess < number):
            print("Too low, try again")

            guess = int(input("Enter your guess: "))

    print("\nCongratulations, you have guessed the number!")


main()
