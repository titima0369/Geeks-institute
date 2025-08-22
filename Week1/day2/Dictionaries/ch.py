user_word = input("Please enter a word: ")

letter_indexes = {letter: [i for i, char in enumerate(user_word) if char == letter] for letter in set(user_word)}

print(letter_indexes)