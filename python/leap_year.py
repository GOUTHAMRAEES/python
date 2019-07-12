def leap(year):
    if(year%4==0):
        if year%400==0 and year%100==0:
            print("{} is a leap year".format(year))
        elif year%100!=0:
            print("{} is a leap year".format(year))
        else:
            print("{} is not a leap year".format(year))

    else:
        print("{} is not a leap year".format(year))

year=int(input("Enter the year: "))
leap(year)
        
