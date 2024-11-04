print("Welcome to Tresure Island.") 
print("Your mission is to find the treasure.") 
choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right".').lower() 
if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?").lower() 
        if choice3 == "red":
            print("it's a room full of fire. gmae over.")
        elif choice3 == "yellow":
            print("you found the treasure! you win!")
        elif choice3 == "blue":
            print("you enter a room of beasts. gmae over.") 
        else:
            print("you choose a door that  doesn't exist. game over.") 
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.") 