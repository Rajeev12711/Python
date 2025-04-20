import pandas as pd

file  = pd.read_csv("nato_phonetic_alphabet.csv")

dicts = {row.letter: row.code for (index, row) in file.iterrows()}

user_input = input("Enter your word: ").upper()

code_words = [dicts[code] for code in user_input]

print(code_words)