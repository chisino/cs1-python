print("This program determines distance traveled using a while loop")

speed = int(input("\nEnter the speed of the vehicle in miles per hour: "))

time = int(input("Enter the number of hours traveled: "))

print("\nHour\tDistance Traveled")

i = 1

while (i <= time):
    print(i,"\t",(speed*i))
    i += 1
