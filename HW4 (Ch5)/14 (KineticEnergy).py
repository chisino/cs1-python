# KE = 1/2mv^2, m = mass (kg), v = velocity (m/s)

def main():
    print("This program calculates kinetic energy\n")

    mass = float(input("Enter the object's mass in kg: "))

    velocity = float(input("Enter the object's velocity in m/s: "))

    kinEnergy = kinetic_energy(mass, velocity)

    print("\nThe object's kinetic energy is",format(kinEnergy, '.2f'))


def kinetic_energy(mass, velocity):
    
    kinEnergy = (.5 * mass) * (velocity ** 2)

    return kinEnergy
    

main()
