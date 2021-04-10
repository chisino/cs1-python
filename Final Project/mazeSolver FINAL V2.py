print("This program opens a maze from a file and solves it")

def main():

    #creating the matrix for the maze

    matrix = matrixCreate('maze.txt')

    cr = 0
    cc = 0

    #finding 'S' (start)

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if ('S' == matrix[i][j]):
                cr = i
                cc = j

    #checking if there is an 'E' in the maze

    eCheck = 0

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if ('E' == matrix[i][j]):
                eCheck = 1
                break

    if (eCheck == 0):
        print("This maze has no end point")
        return 0

    #setting the first square to an x and printing the maze

    matrix[cr][cc] = 'x'

    #loop that solves the maze
    
    direction = '' # up = square up, down = square down
                   # left = square left, right = square right

    while (matrix[cr][cc] != 'E'):

        if ((matrix[cr][cc-1] == '#' or matrix[cr][cc-1] == '.') and (matrix[cr][cc+1] == '#' or matrix[cr][cc+1] == '.')):

            if (matrix[cr-1][cc] == ' '):
            
                direction = 'up'

            elif (matrix[cr+1][cc] == ' '):

                direction = 'down'

        elif ((matrix[cr-1][cc] == '#' or matrix[cr-1][cc] == '.') and (matrix[cr+1][cc] == '#' or matrix[cr+1][cc] == '.')):

            if (matrix[cr][cc+1] == ' '):

                direction = 'right'

            elif (matrix[cr][cc-1] == ' '):

                direction = 'left'

        if (direction == 'up'):
            matrix[cr-1][cc] = 'x'
            matrix[cr][cc] = '.'
            cr = cr-1
            cc = cc

        elif (direction == 'down'):
            matrix[cr+1][cc] = 'x'
            matrix[cr][cc] = '.'
            cr = cr+1
            cc = cc
            
        elif (direction == 'right'):
            matrix[cr][cc+1] = 'x'
            matrix[cr][cc] = '.'
            cr = cr
            cc = cc+1
            
        elif (direction == 'left'):
            matrix[cr][cc-1] = 'x'
            matrix[cr][cc] = '.'
            cr = cr
            cc = cc-1

        #procedures for when 'E' (end) is one square away

        if (matrix[cr][cc+1] == 'E'):

            matrix[cr][cc+1] = 'x'
            matrix[cr][cc] = '.'

            printMatrix(matrix)

            print("The maze has been solved")

            return 0

        elif (matrix[cr][cc-1] == 'E'):

            matrix[cr][cc-1] = 'x'
            matrix[cr][cc] = '.'

            printMatrix(matrix)

            print("The maze has been solved")

            return 0

        elif (matrix[cr-1][cc] == 'E'):

            matrix[cr-1][cc] = 'x'
            matrix[cr][cc] = '.'

            printMatrix(matrix)

            print("The maze has been solved")

            return 0

        elif (matrix[cr+1][cc] == 'E'):

            matrix[cr+1][cc] = 'x'
            matrix[cr][cc] = '.'

            printMatrix(matrix)
            print("The maze has been solved")

            return 0


# This function creates a matrix from the given file
def matrixCreate(fileName):
    f = open(fileName, 'r')

    matrix = [[0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0]]

    item = f.readlines()

    for i in range(0, len(item)):
        item[i] = item[i].rstrip('\n')

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            matrix[i][j] = item[i][j]

    f.close()

    return matrix


# This function prints out the maze
def printMatrix(matrix):
    for r in range(0,len(matrix)):
        for c in range(0,len(matrix)):
            print(matrix[r][c], end='')
        print()


main()
