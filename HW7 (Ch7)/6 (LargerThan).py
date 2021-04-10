print("This program displays numbers in a list that are greater than n")

def main():

    listX = [1,4,6,8,10,12]

    n = 7

    larger(listX, n)


def larger(listX, n):

    for i in range(0, len(listX)):
        if listX[i] > n:
            print(listX[i])
            
    
main()
