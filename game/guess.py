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


"""Guess() class
    Author: Noah Blevins
    Team 02
    CSE210.10
    
    I have created this class such that provided a means of initializing it with a word,
    it is completely self-sustained. If for some reason we need this class later,
    it will work wherever we need to drop it.
    
    Note that neither the word that initializes the class nor the letters guessed are case-sensitive.
    Take that, user error!
    
    Well, I can only partly throw user error out. If the user enters more than one letter, the program breaks.
    Maybe we can implement something in Director that stops the user from entering a guess that's too long?"""

#The Guess() Class should have an instance created like so: var = Guess(word)

class Guess:
    #Initialize with a word variable in the parentheses, or a string literal. Either works.
    def __init__(self, word):
        self._word = word.upper()
        self._guess = []
        for i in range(len(word)):
            self._guess.append('_')
        self._guessString = ' '
        self._index = 0
        self._letter = ''
        
    #Gets the guess, and returns a string that contains all blanks and guessed letters.
    def get_guess(self):
        self._guessString = ' '.join(self._guess)
        return self._guessString

    #The following function is called for two reasons:
    #One, to guess a letter, and two, to return a bool for if the letter is in there
    #Example: object is called var, word is APPLE, and assume Director has a bool is_correct.
    #Usage would then be: is_correct = var.user_guess(letter)
    #If letter == 'A' (not case-sensitive), is_correct = True
    #Additionally, self._guess would replace the first item with 'A'.
    #Calling get_guess would then return A____ if it's the first correct guess, or perhaps A__L_ if L was guessed first.
    #Note that guessing a letter with multiples is taken into account, with a guess of 'p' instead giving us _PP__.
    #Otherwise, if letter == 'z', is_correct = False, and the guess list would not be modified.
    
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
        
    #This checks to see if the word is complete. If it is not, return False. If it is, return True.
    #Its intended purpose is to check to see if the game is over with a win. Parachute() should have something similar,
    #but instead it will check to see if the game is over with a loss.
    def check_word(self):
        if ('_' in self._guess):
            return False
        else:
            return True

"""Note: in order to get this to work, I made a new file for testing and then imported the object.
I never added it to the Git repository, so it's not in there. If you want to see it, though, in order to 
get a better view of how to use the Guess() class, then message me on Slack. And if for some reason you are
someone just browsing randomly through GitHub and not someone on my team, first of all, hello, and second of all,
I unfortunately cannot give it to you. --Noah Blevins"""