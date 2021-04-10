print("This program prints out a table of C and F temperatures using a while loop")

print("\nCelsius\tFahrenheit")

i = 0

while (i <= 20):
    print(i,"\t", format(((i * 1.8) + 32), '.1f'))
    i += 1
