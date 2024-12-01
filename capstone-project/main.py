import random
import math

def game():
    cards =  [1, 2, 3, 4, 5, 6, 7,  8, 9, 10, 10, 10, 10, 11]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) ==2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

user = []
computer = []
game_over = False
for _ in range(0, 2):
    user.append(game())
    computer.append(game())

user_score = calculate_score(user)
computer_score = calculate_score(computer)
print(f" your card: {user}, current score: {user_score}")
print(f" computer first card: {computer[0]}")
if user_score == 0 or computer_score == 0 or user_score>21:
    game_over=True

    
    