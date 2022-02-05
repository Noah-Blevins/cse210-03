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

from game.guess import Guess
from game.parachute import Parachute
from game.words import Words


class Director: 

    def __init__(self):
        self._guess = Guess()
        self._parachute = Parachute()
        self._words = Words()
        
    def start_game(self):
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._give_outputs()

    def _get_inputs(self):
        pass
    def _do_updates(self):
        pass
    def _do_outputs(self):
        pass