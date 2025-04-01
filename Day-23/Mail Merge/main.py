with open("./Input/Names/invited_names.txt","r") as file:
    names = file.readlines()

with open("./Input/Letters/strating_letter.txt", "r") as file2:
    contents = file2.read()
    contents = contents.strip()

for i in range(len(names)):
    name= names[i].strip()
    with open(f"./Output/ReadyToSend/letter_for_{name}", "w") as letter:
        letter.write(contents.replace("[name]", name))
