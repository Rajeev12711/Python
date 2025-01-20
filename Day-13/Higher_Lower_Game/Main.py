import random
import os
from Game_Data import data
from Art import logo, vs

def detail():
  return random.choice(data)

def CompAccount(account):
  name = account["name"]
  country = account["country"]
  description = account["description"]
  return f"{name}, a {description}, from {country}"
  
def checkTheaccount(a,b):
  while a==b:
    b = detail()
  else:
    return b 
  
def check(user, a_follower, b_follower):
  if user == "a" and a_follower > b_follower:
    return True
  elif user == "b" and a_follower < b_follower:
    return True
  else:
    return False

score = 0
game_ongoing = True
a = detail()
b = detail()

while game_ongoing:

  b = checkTheaccount(a,b)

  print(f"Compare A: {CompAccount(a)}")
  print(vs)
  print(f"Against B: {CompAccount(b)}")

  user = input("Who has more follower? Type 'A' or 'B': ").lower()

  a_follower = a["follower_count"]
  b_follower = b["follower_count"]

  correct = check(user, a_follower, b_follower)
  os.system("clear")

  if correct:
    score +=1
    a = b
    b = detail()
    print(f"You're right,! Currrent Score: {score}.")
  else:
    print(f"Sorry, that's wrong. Final Score: {score}")
    
    restart = input("You want to Restrart the game than enter 'Yes' or not than 'No': ").lower()
    if restart == "yes":
      game_ongoing= True
    else:
      game_ongoing = False