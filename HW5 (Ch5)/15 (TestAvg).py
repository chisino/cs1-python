
def main():
    print("This program determines average scores and letter grades of tests\n")

    test1 = int(input("Enter the first test score: "))
    test2 = int(input("Enter the second test score: "))
    test3 = int(input("Enter the third test score: "))
    test4 = int(input("Enter the fourth test score: "))
    test5 = int(input("Enter the fifth test score: "))
    
    print("\n")

    print(test1)
    determine_grade(test1)

    print("\n")

    print(test2)
    determine_grade(test2)

    print("\n")

    print(test3)
    determine_grade(test3)

    print("\n")

    print(test4)
    determine_grade(test4)

    print("\n")

    print(test5)
    determine_grade(test5)

    avgScore = calc_average(test1,test2,test3,test4,test5)

    print("\nThe average score is",avgScore)
   
    
def calc_average(test1,test2,test3,test4,test5):
    
    return ((test1+test2+test3+test4+test5) / 5)


def determine_grade(test):

    if (90 <= test <= 100):
        print("A")
    elif (80 <= test <= 89):
        print("B")
    elif (70 <= test <= 79):
        print("C")
    elif (60 <= test <= 69):
        print("D")
    elif (test < 60):
        print("F")
    else:
        print("This test score is invalid")


main()
