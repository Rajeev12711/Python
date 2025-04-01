file = open("new_text.txt")
contents = file.read()
print(contents)
file.close()

with open("text.txt", mode="w") as file:
    file.write("This is a for Python Practices.")


with open("new_text.txt", mode="a") as file:
    file.write("\nThis is a for Python Practices.")
