height = int(input("Enter your height: "))

if height >= 120:
    print("You can ride the rollercoaster!") 
    age=int(input("What is your age? "))
    if age <12:
        bill=5
        print("Child tickets are $5.") 
    elif age <= 18:
        bill=7 
        print("Youth tickets are $7.")
    else:
        bill=12
        print("Adult tickets are $12.") 
    
    wants_photo = input("Do you want a photo taken? Y or N.: ").lower
    if  wants_photo =="y":
        bill+=3
        print("$3 extra for photo.")
    
    print("Your bill is", bill)
else:
    print("Sorry, You have to grow taller before you can ride this.")