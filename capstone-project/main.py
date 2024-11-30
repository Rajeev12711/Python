import random
import math

def game():
    cards =  [1, 2, 3, 4, 5, 6, 7,  8, 9, 10, 10, 10, 10, 11]
    card = random.choice(cards)
    return card

user = []
computer = []
for _ in range(0, 2):
    user.append(game())
    computer.append(game())

print(computer, user)


def calculate_score(cards):
    return sum(cards)

score=calculate_score(cards)
print(score)

        





