print("This program decrypts files")

def main():

    codes = {'A':'1','a':'!','B':'2','b':'@','C':'3','c':'#','D':'4','d':'$','E':'5','e':'%',
             'F':'6','f':'^','G':'7','g':'&','H':'8','h':'*','I':'9','i':'(','J':'0','j':')',
             'K':'-','k':'_','L':'=','l':'+','M':'[','m':'{','N':']','n':'}','O':';','o':':',
             'P':',','p':'<','Q':'.','q':'>','R':'/','r':'?','T':'`','t':'~','U':'U_','u':'u_',
             'V':'V_','v':'v_','W':'W_','w':'w_','X':'X_','x':'x_','Y':'Y_','y':'y_','Z':'Z_','z':'z_'}


    codeList = list(codes)

    file = open('encryptFile.txt', 'r')

    encFile = open('decryptedFile.txt', 'w')

    text = file.read()

    i = 0
    j = 0

    while i < len(text):
        while j < len(codeList):
            key = codeList[j]
            if i == len(text):
                break
            if (text[i] == codes[key]):
                encFile.write(key)
                i += 1
                j = 0
            else:
                j += 1

    print("\nThe file has been decrypted and saved to a new file")

    file.close()
    encFile.close()

    
main()
