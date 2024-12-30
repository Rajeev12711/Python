import random 
import os

def game():
    cards =  [2, 3, 4, 5, 6, 7,  8, 9, 10, 10, 10, 10, 11]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) ==2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's Draw"
    elif computer_score == 0:
        return "The User Loses."
    elif user_score == 0:
        return "The User Wins."
    elif user_score >21:
        return "The User Loses."
    elif computer_score >21:
        return "The User Wins."
    elif user_score > computer_score:
        return "The User Wins."
    else:
        return "The User loses"

def start():
    user = []
    computer = []
    game_over = False
    for _ in range(0, 2):
        user.append(game())
        computer.append(game())

    while not game_over: 
        user_score = calculate_score(user)
        computer_score = calculate_score(computer)
        print(f" Your Card: {user}, Current Score: {user_score}")
        print(f" Computer First Card: {computer[0]}")
        if user_score == 0 or computer_score == 0 or user_score>21:
            game_over=True
        else:
            user_new_card = input("If you want to draw a another card than enter 'Yes' or not than 'No': ").lower()
            if user_new_card =='yes':
                user.append(game())
            else:
                game_over = True

    while computer != 0 and computer_score < 17:
        computer.append(game())
        computer_score = calculate_score(computer)

    print(f" Your Final Cards: {user}, Final Score: {user_score}")
    print(f" Computer Final Cards: {computer}, Final Score: {computer_score}")
    print(compare(user_score, computer_score))

while True:
    play_game = input("Do you want to play a game of Black Jack? Type 'yes' or 'no': ").lower()
    if play_game == 'yes':
        os.system('clear')
        start()
    elif play_game == 'no':
        print("Thanks for playing! Goodbye.")
        break
    