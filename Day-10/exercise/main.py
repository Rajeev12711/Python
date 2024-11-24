def leap(year):
    if  year % 4 ==0:
        if year % 100 == 0:
            if year % 400 ==0:
                return True
            else :
                return False
        else:
            return True
    else:
        return False

def day_month(year, month):
    if month>0 and month<=12:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        return "Invalid Number"
    if leap(year)== True and month == 2:
        return 29
    else:
        return months[month -1]

year = int(input("Enter a year: "))
month = int(input("Enter a month(number): "))

print(day_month(year, month))