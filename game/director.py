# Specifications:

# •	Director class
#     o	Method start_game() that contains and continually calls three methods, get_inputs(), do_updates(), give_outputs()
#     o	__init__ will get a word from Words(), creates an instance of Guess(), and create a new instance of Parachute().
#     o	Call Guess.get_guess() in get_inputs()
#     o	Check if the guess is correct with Guess() in do_updates()
#     o	Check if the guess is incorrect with Parachute in do_updates()
#     o	Print the current guess and parachute in give_outputs()
#     o	If game is over according to Guess() or Parachute(), end the gameplay loop in start_game()
