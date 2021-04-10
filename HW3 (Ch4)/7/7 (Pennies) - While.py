print("This program prints out a table of salaries that double using a while loop")

days = int(input("\nEnter the number of days: "))

print("\nDay\tSalary")

salary = .01

print(1,"\t$",salary) #printing out the initial salary before loop

i = 2 #starting loop at 2nd day

while (i <= days):
    salary *= 2
    print(i,"\t$",salary)
    i += 1
    
    
    


