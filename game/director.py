# Specifications:

# •	Director class
#     o	Method start_game() that contains and continually calls three methods, get_inputs(), do_updates(), give_outputs()
#     o	__init__ will get a word from Words(), creates an instance of Guess(), and create a new instance of Parachute().
#     o	Call Guess.get_guess() in get_inputs() (NOT TRUE ANYMORE)
#     o	Check if the guess is correct with Guess() in do_updates()
#     o	Check if the guess is incorrect with Parachute in do_updates()
#     o	Print the current guess and parachute in give_outputs()
#     o	If game is over according to Guess() or Parachute(), end the gameplay loop in start_game()
#
#     IGNORE THE ABOVE
#     
#     __init__ will create instances of all other classes
#     start_game() will contain all other non-init methods
#     _get_inputs() will run Guess.get_guess()
#     _do_updates() runs all update methods in parachute and guess, including an exit if the
#       parachute is fully gone or the word is fully guessed
#     _give_outputs() prints the parachute and the current word state
#       We also want something extra to signal the game has ended, but this can be in start_game()      
#       We will use Encapsulation throughout

"""Director() class
    Author: Ashton Pieterse
    Team 02
    CSE210.10
    
    This class connects all other classes in order for the game to operate. It uses encapsulation throughout. 
    The start_game function runs the game. It calls the get_input, do_updates and give_outputs.
    Get_inputs asks the user to provide an input. It will keep asking unless a user provides a valid input(single letter, no spaces or characters).
    Do_updates checks if the input is in the word(via guess). If it is not then a part of the parachute is removed(parachute).
    Give_outputs prints the blank words and correct guessed words, as well as draws the parachute. 
    """

from game.guess import Guess
from game.parachute import Parachute
from game.words import Words


class Director: 

    def __init__(self):
        self._words = Words()
        # New line below
        self._word = self._words.get_word()
        self._guess = Guess(self._word)
        self._parachute = Parachute()
        self._is_playing = True
        self._first_play = True
        self.winning = False
        self.losing = False
        self._new_letter = " "
        
    def start_game(self):
        while self._is_playing:
            while self._first_play: 
                self._give_outputs()
                self._first_play = False
            self._get_inputs()
            self._do_updates()
            self._give_outputs()
            

    def _get_inputs(self):
        guess = input("Guess a letter [a-z]:")
        while guess.isalpha() != True or len(guess) != 1:
            guess = input("You entered an invalid letter. Please guess a single letter [a-z]:")
                
        self._new_letter = guess

        
    def _do_updates(self):
        self._parachute.break_parachute(self._guess.user_guess(self._new_letter))
        self.winning = self._guess.check_word()
        self.losing = self._parachute.parachute_broken()
        
    def _give_outputs(self):
        word = self._guess.get_guess()
        self._parachute.draw_parachute()
        print(f"{word}")

        if self.winning:
            self._is_playing = False
            print("You guessed it! Play again soon!")

        elif self.losing:
            self._is_playing = False
            print("Im afraid you lost your parachute! Better luck next time.")

        else:
            self._is_playing = True

        
