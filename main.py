import pandas as pd

# Read the CSV file and set the "letter" column as the index
df = pd.read_csv("./data/nato_phonetic_alphabet.csv", index_col="letter")

# Create a dictionary in this format: {"A": "Alfa", "B": "Bravo", ...}
nato_phonetic = {alpha: word.iloc[0] for (alpha, word) in df.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
going_on = True
while going_on:
    # Prompt the user to input a word and convert it to uppercase
    word = input("Enter your word: ").upper()
    try:
        # Generate a list of phonetic code words for each letter in the input word
        nato_list = [nato_phonetic[letter] for letter in word]
        print(nato_list)
    except KeyError:
        # Handle cases where the input contains non-alphabet characters
        print("Sorry, only in the alphabet please.")

    # Exit the loop if the user inputs "EXIT"
    if word == "EXIT":
        going_on = False
