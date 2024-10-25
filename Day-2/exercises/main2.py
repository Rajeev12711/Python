height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

height = float(height)
weight = float(weight)

bmi = int(weight / height ** 2)
print(bmi)