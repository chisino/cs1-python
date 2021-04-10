def main():
    print("This program creates a personal web page\n")

    name = input("Enter your name: ")

    desc = input("Describe yourself: ")

    htmlFile = open("webpage.html","w")

    htmlCreate(htmlFile, name, desc)

    print("\nThe html file has been created")

    htmlFile.close()

def htmlCreate(htmlFile, name, desc):
    htmlFile.write("<html>" + "\n")
    htmlFile.write("<head>" + "\n")
    htmlFile.write("< /head>" + "\n")
    htmlFile.write("<body>" + "\n")
    htmlFile.write("\t<center>" + "\n")
    htmlFile.write("\t\t<h1>")
    htmlFile.write(name)
    htmlFile.write("<h1>" + "\n")
    htmlFile.write("\t<center>" + "\n")
    htmlFile.write("\t<hr />" + "\n")
    htmlFile.write("\t")
    htmlFile.write(desc)
    htmlFile.write("\n")
    htmlFile.write("\t<hr />" + "\n")
    htmlFile.write("<body>" + "\n")
    htmlFile.write("</html>" + "\n")


main()
