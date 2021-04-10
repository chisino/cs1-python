# d = 1/2gt^2, d = distance, g = 9.8, t = time in seconds

def main():
    print("This program calculates the distance an object falls because of gravity\n")

    fallTime = 1

    while (fallTime <= 10):

        distance = falling_distance(fallTime)

        print(format(distance, '.2f'))
        
        fallTime +=  1


def falling_distance(fallTime):

    distance = (.5 * 9.8) * (fallTime ** 2)

    return distance


main()
