year = int(input("Enter a year: "))

if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f"{year} is leap year.")
        else:
            print(f"{year} not is leap year.")
    else:
        print(f"{year} is leap year.")
else:
    print(f"{year} not is leap year.")