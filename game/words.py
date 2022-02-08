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
        self.word_list = ["power", "laptop", "vehicle", "tophat", "moter", "robot", "soccer", "cheese", "gameboy", "sword", "slasher",
         "flower", "havoc", "seabear", "sponge", "circle", "square", "catfish", "tissue", "words"]

    def get_word(self,):
        return random(self.word_list)
