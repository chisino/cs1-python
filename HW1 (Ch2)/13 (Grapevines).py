print("This program calculates the number of grapevines that will fit in a row\n")

lengthRow = float(input("Enter the length of the row, in feet: "))

assemblySpace = float(input("Enter the amount of space used by the end-post assembly, in feet: "))

vineSpace = float(input("Enter the amount of space between the vines, in feet: "))

#V = R-2ES
#R = lengthRow, E = assemblySpace, S = vineSpace

numVines = (lengthRow - (2 * assemblySpace)) / vineSpace

print("\nThe number of grapevines that will fit in the row is",format(numVines, '.2f'))
