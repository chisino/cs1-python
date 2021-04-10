print("This program determines distance traveled using a for loop")

speed = int(input("\nEnter the speed of the vehicle in miles per hour: "))

time = int(input("Enter the number of hours traveled: "))

print("\nHour\tDistance Traveled")

for i in range (1, time + 1, 1):
    print(i,"\t",(speed*i))
    
