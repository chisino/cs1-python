print("This program opens a maze from a file and solves it")

def main():

    matrix = matrixCreate('maze.txt')

    cr = 0
    cc = 0

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if ('S' == matrix[i][j]):
                cr = i
                cc = j

    direction = ''

    for x in matrix:
        print(x)
    print()

    matrix[cr][cc] = 'x'

    for x in matrix:
        print(x)
    print()

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

        for x in matrix:
            print(x)
        print()

        if (matrix[cr][cc+1] == 'E'):

            matrix[cr][cc+1] = 'x'
            matrix[cr][cc] = '.'

            for x in matrix:
                print(x)
            print()

            print("The maze has been solved")

            return 0

        elif (matrix[cr][cc-1] == 'E'):

            matrix[cr][cc-1] = 'x'
            matrix[cr][cc] = '.'

            for x in matrix:
                print(x)
            print()

            print("The maze has been solved")

            return 0

        elif (matrix[cr-1][cc] == 'E'):

            matrix[cr-1][cc] = 'x'
            matrix[cr][cc] = '.'

            for x in matrix:
                print(x)
            print()

            print("The maze has been solved")

            return 0

        elif (matrix[cr+1][cc] == 'E'):

            matrix[cr+1][cc] = 'x'
            matrix[cr][cc] = '.'

            for x in matrix:
                print(x)
            print()

            print("The maze has been solved")

            return 0


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


main()
