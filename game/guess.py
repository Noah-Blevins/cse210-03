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

class Guess:

    def __init__(self, word):
        self._word = word.upper()
        self._guess = []
        for i in range(len(word)):
            self._guess.append('_')
        self._guessString = ''
        self._index = 0
        self._letter = ''

    def get_Guess(self):
        self._guessString = ''.join(self._guess)
        return self._guessString

    def user_guess(self, letter):
        self._letter = letter.upper()
        for i in range(len(self._guess)):
            self._index = self._word.find(self._letter, self._index)
            if self._index == -1:
                break
            if self._letter in self._word:
                self._guess[self._index] = self._letter
            self._index += 1
        self._index = 0
        if self._letter in self._guess:
            return True
        else:
            return False

    def check_word(self):
        if ('_' in self._guess):
            return False
        else:
            return True

