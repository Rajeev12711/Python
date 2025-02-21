height = float(input("enter the height in m?"))
weight = float(input("enter the weight in kg?"))
bmi = weight/height ** 2 
if bmi<18.5:
    print("Your bmi is " ,bmi,". You are under weight." )
elif 18.5<bmi<25:
    print("Your bmi is " ,bmi, ". You normal weight.")
elif 25<bmi<30:
    print("Your bmi is " ,bmi, ". You slightly overweight.")
elif 30<bmi<35:
    print("Your bmi is " ,bmi, ". You are obesity.")
15