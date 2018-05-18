#Ezekial Page
#calculates day of the week given any month day and year

print("This program will tell the day of the week for any given date.")
print("Enter 0 at any point to exit the program")
run = 0
while(run != 1):
    print("")
    month = int(input("Enter month: "))
    if month == 0:
        print("Program terminated.")
        break
    day = int(input("Enter day: "))
    if day == 0:
        print("Program terminated.")
        break
    year = int(input("Enter year: "))
    if year == 0:
        print("Program terminated.")
        break

    if month == 1 or month == 2:
        month = month + 12
        year = year - 1

    a = month * 2
    b = ((month + 1) * 3)//5
    c = year // 4
    d = year // 100
    e = year // 400
    f = 2 + day + year + a + b + c + e
    g = f - d
    h = g % 7

    if h == 0:
        weekDay = "Saturday"
    elif h == 1:
        weekDay = "Sunday"
    elif h == 2:
        weekDay = "Monday"
    elif h == 3:
        weekDay = "Tuesday"
    elif h == 4:
        weekDay = "Wednesday"
    elif h == 5:
        weekDay = "Thursday"
    else:
        weekDay = "friday"
    if month == 13 or month == 14:
        if (year < (2016)) or (year == 2016):
            print("The day " + str(month-12) + "/" + str(day) + "/" + str(year + 1) + " was a " + weekDay)
        else:
            print("The day " + str(month-12) + "/" + str(day) + "/" + str(year + 1) + " will be a " + weekDay)
    else:
        if (year < 2017) or ((year == 2017) and (month < 10)):
            print("The day " + str(month) + "/" + str(day) + "/" + str(year) + " was a " + weekDay)
        else:
            print("The day " + str(month) + "/" + str(day) + "/" + str(year) + " will be a " + weekDay)

        
