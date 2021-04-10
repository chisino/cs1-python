print("This program handles names and email addresses")

import pickle

def main():

    initial = input("Type y to see current dictionary: ")

    if (initial == 'y'):
        try:
            fileRead = open('emails.dat', 'rb')
            emp = pickle.load(fileRead)
            print(emp)
            fileRead.close()
        except(EOFError):
            print("Dictionary cannot be empty - make an entry first")

    file = open('emails.dat', 'wb')
    
    mailList = makeList()
    menu(mailList)
    pickle.dump(mailList, file)
    
    file.close()


def makeList():
    mailList = {}
    again = 'y'
    while again == 'y':
        name = input('Enter a name: ')
        email = input('Enter the email address: ')
        mailList[name] = email
        again = input('Enter y to add more: ')
        
    return mailList

def menu(mailList):
    again = 'y'
    while again == 'y':
        selectMenu = input('1 : Look Up, 2: Add, 3: Change, 4: Delete, or n: ')
        if selectMenu == '1':
            mailList = lookUp(mailList)

        elif selectMenu == '2':
            mailList = add(mailList)

        elif selectMenu == '3':
            mailList = change(mailList)

        elif selectMenu == '4':
            mailList = delete(mailList)

        elif selectMenu == 'n':
            again = 'n'
            
def lookUp(mailList):
    name = input('Enter a name: ')
    print(mailList[name])
    
    return mailList

def add(mailList):
    name = input('Enter a name: ')
    email = input('Enter the email address: ')
    mailList[name] = email
         
    return mailList

def change(mailList):
    name = input('Enter a name: ')
    print(mailList[name])
    again = input('Enter y to make a change: ')
    if again == 'y':
        email = input('Enter the email address: ')
        mailList[name] = email
         
    return mailList

def delete(mailList):
    name = input('Enter a name: ')
    print(mailList[name])
    again = input('Enter y to delete this address: ')
    if again == 'y':
        del mailList[name]
         
    return mailList


main()
