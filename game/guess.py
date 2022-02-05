# Specifications:

# •	Guess class
#     o	Gets a user-defined word upon initialization
#       Compares the guess from the user to the word and fills in spots accordingly
#     o	Prints blanks, as well as the correct letters guessed
#     o	A method to determine if the word is guessed

# On init, create list[] of blanks as long as word provided. Note that the init should have __init__(self, word)
# It would be called by guess = Guess(whatever variable we are using)

# get_guess(self, some variable to mean the guessed letter) gets and returns the blanks and correct letters
# user_guess() takes the letter the user guessed and will edit the list[] accordingly
# user_guess() will also return a bool based on if the letter was in the word
# check_word() returns True if the word is completely guessed