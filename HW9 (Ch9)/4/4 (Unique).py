print("This program finds the unique words in a file")

def main():

    file = open('unique.txt', 'r')

    fileContents = file.read()

    wordList = fileContents.split()
    
    uniqueWords = set(wordList)
    
    for i in uniqueWords:
        print(i)
        

    file.close()


main()
