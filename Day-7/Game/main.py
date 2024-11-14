import random

words = ["andhrapradesh", "arunachalpradesh", "assam", "bihar", "chhattisgarh", "goa", "gujarat", "haryana", "himachalpradesh", "jharkhand", "karnataka", "kerala", "madhyapradesh", "maharashtra", "manipur", "meghalaya", "mizoram", "nagaland", "odisha", "punjab", "rajasthan", "sikkim", "tamilnadu", "telangana", "tripura", "uttarakhand", "uttarpradesh", "westbengal"]
word=random.choice(words)
num = len(word)

life = 4

empty =[]
for display in range(num):
    empty += "_" 
                 
end_game = False

while not end_game:
    guess =input("Guess The Indian State By Letter!\n").lower()
    for index in range(len(word)):
        letter = word[index]
        if guess==letter:
            empty[index]=letter
    if guess not in word:
        life -= 1
        print(f"You Lose a life Because You Guess Worng Letter {guess}. Now You Left {life} life")
        if life == 0:
            end_game = True
            print("You Lose")

    print(empty)
    
    if "_" not in empty:
        end_game = True 
        print("You Win")
