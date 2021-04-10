print("This program displays the percentages of males and females in a class\n")

maleNum = int(input("Enter the number of males in the class: "))

femaleNum = int(input("Enter the number of females in the class: "))

total = maleNum + femaleNum

malePercent = (maleNum / total) * 100

femalePercent = (femaleNum / total) * 100

print("\nThe percentage of males in the class is",format(malePercent, '.2f'), "%")

print("The percentage of females in the class is",format(femalePercent, '.2f'), "%")
