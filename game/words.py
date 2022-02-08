# Specifications:

# •	Words class
#     o	Has a list of words
#     o	Gets a random word from the list

# Initialize with a list[]
# If we use an external .txt for words, make a method to populate the list
# If internal, populate during __init__

# get_word() will return a word from the list


import random
class Words:
    
    def __init__(self):
        # This init will populate a list wide variety of words between 5 and 7 letters long for the use of the get word method.
        self._word_list = ["power", "laptop", "vehicle", "tophat", "moter", "robot", "soccer", "cheese", "gameboy", "sword", "slasher",
         "flower", "havoc", "seabear", "sponge", "circle", "square", "catfish", "tissue", "words"]

    def get_word(self,):
        # get_word simply returns a random word from word_list
        return random(self._word_list)
