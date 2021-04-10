print("This program generates a 7-digit lottery number")

import random

MIN = 0
MAX = 9

def main():
    num1 = random.randint(MIN,MAX)
    num2 = random.randint(MIN,MAX)
    num3 = random.randint(MIN,MAX)
    num4 = random.randint(MIN,MAX)
    num5 = random.randint(MIN,MAX)
    num6 = random.randint(MIN,MAX)
    num7 = random.randint(MIN,MAX)

    lotteryList = [num1, num2, num3, num4, num5, num6, num7]

    print()

    for i in range(0, len(lotteryList)):
        print(lotteryList[i], end = ' ')


main()
