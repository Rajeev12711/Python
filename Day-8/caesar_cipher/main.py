letters =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def crypt(text, shift, choice):
    final =  ""
    if choice == "decode":
        shift *= -1
    for letter in text:
        if letter  in letters:
            position = letters.index(letter)
            new_position = position + shift
            final += letters[new_position]
        else:
            final += letter        
    print(f"This is your {choice} text {final}")



again =True

while again:
    choice =input("choices between 'encode' or 'decode': ")
    text = input("Type a message: \n").lower()
    shift = int(input("Enter the Number of shit use in 'encode' or 'decode:'\n"))
    shift= shift%26 
    crypt(text, shift, choice)
    reuse = input("Do want to reuse the program than type 'yes' or if not than 'no'.")      
    if reuse =="no":
        again=False
        print("Good Bye")
