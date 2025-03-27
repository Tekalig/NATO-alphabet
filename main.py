import pandas as pd

df = pd.read_csv("./data/nato_phonetic_alphabet.csv", index_col="letter")

# Create a dictionary in this format:
nato_phonetic = {alpha: word.iloc[0] for (alpha, word) in df.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
going_on = True
while going_on:

    word = input("Enter your word: ").upper()
    try:
        nato_list = [nato_phonetic[letter] for letter in word]
        print(nato_list)
    except KeyError:
        print("Sorry, only in the alphabet please.")

    if word == "EXIT":
        going_on = False
