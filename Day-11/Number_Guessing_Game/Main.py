import random

def  random_num():
    return random.randint(1,100)
    

def check(number, user):
    if number < user:
        print("Too High.")
    elif number > user:
        print("Too Low.")
    elif number == user:
        print(F"You got it! The answer is {number}")

def levels(level):
    if level == "easy":
        return 9
    elif level == "medium":
        return 6
    elif level == "hard":
        return 3
    else:
        print("Invalid level. Defaulting to 'easy'.")
        return 9

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    level = input("Choose a difficulty. Enter 'Easy' or 'Medium' or 'Hard': ").lower()
    moves= levels(level)
    number = random_num()
    print(f"You have {moves} attempt to guess the number.")

    user=0
    while user != number:
        user = int(input("Make a guess: "))
        check(number, user)
        
        moves-=1
        if user != number and moves > 0:
            print(f"You have {moves} attempt remaining to guess the number.")
            print("Guess again.")
        elif moves == 0 and user != number:
            return f"You've run out of moves. You lose. The number was {number}."   
        elif user == number:
            return f"You got it. The answer is {number}"
            
print(game())