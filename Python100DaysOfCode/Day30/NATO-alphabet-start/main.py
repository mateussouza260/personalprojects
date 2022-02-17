import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

while True:
    try:
        user_input = input("Enter a word: ").upper()
        phonetic_code = [nato_dict[letter] for letter in user_input]
        print(phonetic_code)
        break
    except KeyError:
        print("Sorry, only letters in the alphabet please")


