import random
letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
sletters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r", "s","t","u","v","w","x","y","z"]
symbols=["!","@","#","$","%","^","&","*","(",")","*","+","="]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
print("Welcome to the Password Creater")
nr_letters = int(input("How many Capital Letters would you like? \n"))
nr_sletters = int(input("How many Small letters would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#  Easy Pasword
# password=""

# for l in range(1,nr_letters+1):
#     password += random.choice(letters)

# for s in range(1,nr_sletters+1):
#     password += random.choice(sletters)

# for sym in range(1,nr_symbols+1):
#     password += random.choice(symbols)

# for num in range(1, nr_numbers+1):
#     password += random.choice(numbers)

# print(password)


# Hard Password
password_list=[]

for l in range(1,nr_letters+1):
    password_list += random.choice(letters)

for s in range(1,nr_sletters+1):
    password_list += random.choice(sletters)

for sym in range(1,nr_symbols+1):
    password_list += random.choice(symbols)

for num in range(1, nr_numbers+1):
    password_list += random.choice(numbers)
    
final=""

random.shuffle(password_list) 

for he  in password_list:
    final += he
    print(final)

print("Your Password:",final)
