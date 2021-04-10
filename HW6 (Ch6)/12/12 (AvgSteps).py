def main():
    print("This program displays the avg number of steps taken each month\n")

    step_file = open("steps.txt","r")

    jan = monthAvg(31, step_file)
    feb = monthAvg(28, step_file)
    mar = monthAvg(31, step_file)
    apr = monthAvg(30, step_file)
    may = monthAvg(31, step_file)
    june = monthAvg(30, step_file)
    july = monthAvg(31, step_file)
    aug = monthAvg(31, step_file)
    sept = monthAvg(30, step_file)
    octbr = monthAvg(31, step_file)
    nov = monthAvg(30, step_file)
    dec = monthAvg(31, step_file)

    print("January:",format(jan,'.2f'))
    print("February:",format(feb,'.2f'))
    print("March:",format(mar,'.2f'))
    print("April:",format(apr,'.2f'))
    print("May:",format(may,'.2f'))
    print("June:",format(june,'.2f'))
    print("July:",format(july,'.2f'))
    print("August:",format(aug,'.2f'))
    print("September:",format(sept,'.2f'))
    print("October:",format(octbr,'.2f'))
    print("November:",format(nov,'.2f'))
    print("December:",format(dec,'.2f'))


    step_file.close()


def monthAvg(days, file):
    contents = int(file.readline())

    total = contents

    i = 1

    counter = 1

    while i < days:
        total += int(file.readline())
        i += 1
        counter += 1
        
    avg = total / counter

    return avg
    

main()
