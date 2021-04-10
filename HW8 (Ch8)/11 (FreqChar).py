print("This program finds the most frequent character in a string")

def main():
    try:
        word = input("\nEnter any word: ")

        FreqFind(word)

    except(ValueError):
        print("String entered must be valid")


def FreqFind(word):
        aCount = 0
        bCount = 0
        cCount = 0
        dCount = 0
        eCount = 0
        fCount = 0
        gCount = 0
        hCount = 0
        iCount = 0
        jCount = 0
        kCount = 0
        lCount = 0
        mCount = 0
        nCount = 0
        oCount = 0
        pCount = 0
        qCount = 0
        rCount = 0
        sCount = 0
        tCount = 0
        uCount = 0
        vCount = 0
        wCount = 0
        xCount = 0
        yCount = 0
        zCount = 0

        for i in range(0, len(word)):
            if word[i] == 'A' or word[i] == 'a':
                aCount += 1
            elif word[i] == 'B' or word[i] == 'b':
                bCount += 1
            elif word[i] == 'C' or word[i] == 'c':
                cCount += 1
            elif word[i] == 'D' or word[i] == 'd':
                dCount += 1
            elif word[i] == 'E' or word[i] == 'e':
                eCount += 1
            elif word[i] == 'F' or word[i] == 'f':
                fCount += 1
            elif word[i] == 'G' or word[i] == 'g':
                gCount += 1
            elif word[i] == 'H' or word[i] == 'h':
                hCount += 1
            elif word[i] == 'I' or word[i] == 'i':
                iCount += 1
            elif word[i] == 'J' or word[i] == 'j':
                jCount += 1
            elif word[i] == 'K' or word[i] == 'k':
                kCount += 1
            elif word[i] == 'L' or word[i] == 'l':
                lCount += 1
            elif word[i] == 'M' or word[i] == 'm':
                mCount += 1
            elif word[i] == 'N' or word[i] == 'n':
                nCount += 1
            elif word[i] == 'O' or word[i] == 'o':
                oCount += 1
            elif word[i] == 'P' or word[i] == 'p':
                pCount += 1
            elif word[i] == 'Q' or word[i] == 'q':
                qCount += 1
            elif word[i] == 'R' or word[i] == 'r':
                rCount += 1
            elif word[i] == 'S' or word[i] == 's':
                sCount += 1
            elif word[i] == 'T' or word[i] == 't':
                tCount += 1
            elif word[i] == 'U' or word[i] == 'u':
                uCount += 1
            elif word[i] == 'V' or word[i] == 'v':
                vCount += 1
            elif word[i] == 'W' or word[i] == 'w':
                wCount += 1
            elif word[i] == 'X' or word[i] == 'x':
                xCount += 1
            elif word[i] == 'Y' or word[i] == 'y':
                yCount += 1
            elif word[i] == 'Z' or word[i] == 'z':
                zCount += 1

        alphList = [aCount, bCount, cCount, dCount, eCount, fCount, gCount, hCount, iCount, jCount, kCount, lCount, mCount, nCount, oCount, pCount, qCount, rCount, sCount, tCount, uCount, vCount, wCount, xCount, yCount, zCount]

        if max(alphList) == aCount:
            print('The most frequent character is a')
        elif max(alphList) == bCount:
            print('The most frequent character is b')
        elif max(alphList) == cCount:
            print('The most frequent character is c')
        elif max(alphList) == dCount:
            print('The most frequent character is d')
        elif max(alphList) == eCount:
            print('The most frequent character is e')
        elif max(alphList) == fCount:
            print('The most frequent character is f')
        elif max(alphList) == gCount:
            print('The most frequent character is g')
        elif max(alphList) == hCount:
            print('The most frequent character is h')
        elif max(alphList) == iCount:
            print('The most frequent character is i')
        elif max(alphList) == jCount:
            print('The most frequent character is j')
        elif max(alphList) == kCount:
            print('The most frequent character is k')
        elif max(alphList) == lCount:
            print('The most frequent character is l')
        elif max(alphList) == mCount:
            print('The most frequent character is m')
        elif max(alphList) == nCount:
            print('The most frequent character is n')
        elif max(alphList) == oCount:
            print('The most frequent character is o')
        elif max(alphList) == pCount:
            print('The most frequent character is p')
        elif max(alphList) == qCount:
            print('The most frequent character is q')
        elif max(alphList) == rCount:
            print('The most frequent character is r')
        elif max(alphList) == sCount:
            print('The most frequent character is s')
        elif max(alphList) == tCount:
            print('The most frequent character is t')
        elif max(alphList) == uCount:
            print('The most frequent character is u')
        elif max(alphList) == vCount:
            print('The most frequent character is v')
        elif max(alphList) == wCount:
            print('The most frequent character is w')
        elif max(alphList) == xCount:
            print('The most frequent character is x')
        elif max(alphList) == yCount:
            print('The most frequent character is y')
        elif max(alphList) == zCount:
            print('The most frequent character is z')


main()
