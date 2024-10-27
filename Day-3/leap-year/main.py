year = int(input("enter a year"))
# year = 2002
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(" is leap year")
        else:
            print(" not is leap year")
    else:
        print(" is leap year")
else:
    print(" not is leap year")