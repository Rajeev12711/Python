numbers = [1,2,3,4,5]
new_numbers =[i +1 for i in numbers]
print(new_numbers)

name = "Rajeev"
letter_list = [letter for letter in name]
print(letter_list)

list_of_table=[number*2 for number in range(1, 5)]
print(list_of_table)

num = [ number for number in range(10) if number <= 5]
print(num)

names = ["Rajeev", "Anurag", "Rupesh", "Ashish" , "Amit"]
new_names = [name.upper() for name in names if len(name)>5 ]
print(new_names)