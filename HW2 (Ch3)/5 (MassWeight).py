print("This program determines if an object is too heavy or too light")

mass = float(input("\nEnter the mass of an object in kg: "))

weight = mass * 9.8

if (weight > 500):
    print("\nThe object is too heavy")
elif (weight < 100):
    print("\nThe object is too light")
else:
    print("\nThe object is neither too heavy nor too light")
