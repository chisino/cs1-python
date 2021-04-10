print("This program classifies a person's age into infant, child, teen, or adult")

age = float(input("\nEnter the person's age: "))

if (age <= 1):
    print("\nThe person is an infant")
elif (age > 1  and age < 13):
    print("\nThe person is a child")
elif (age >= 13 and age < 20):
    print("\nThe person is a teenager")
else:
    print("\nThe person is an adult")

    
