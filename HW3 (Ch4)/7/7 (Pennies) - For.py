print("This program prints out a table of salaries that double using a for loop")

days = int(input("\nEnter the number of days: "))

print("\nDay\tSalary")

salary = .01

print(1,"\t$",salary) #printing out the initial salary before loop

for i in range (2, days + 1, 1): #starting loop at 2nd day
    salary *= 2
    print(i,"\t$",salary)
