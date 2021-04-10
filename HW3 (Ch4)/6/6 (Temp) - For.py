print("This program prints out a table of C and F temperatures using a for loop")

print("\nCelsius\tFahrenheit")

for i in range (0, 20, 1):
    print(i,"\t", format(((i * 1.8) + 32), '.1f'))
