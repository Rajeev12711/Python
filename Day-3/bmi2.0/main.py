height = float(input("enter the height in m?"))
weight = float(input("enter the weight in kg?"))
bmi = weight/height ** 2 
if bmi<18.5:
    print("yoour bmi is " ,bmi ,"your normal weight" )
elif 18.5<bmi<25:
    print("yoour bmi is " ,bmi, "your normal weight")
elif 25<bmi<30:
    print("yoour bmi is " ,bmi, "your normal weight")
elif 30<bmi<35:
    print("yoour bmi is " ,bmi, "your normal weight")
elif 35<bmi:
    print("yoour bmi is " ,bmi, "your normal weight")