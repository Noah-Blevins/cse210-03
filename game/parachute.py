# Specifications:

# •	Parachute class
#     o	Creates the parachute
#       A method to print the current parachute
#     o	A method to eliminate pieces
#     o	A method to determine if pieces are left

# On init, create the parachute
# break_parachute(value) will remove a cord from the parachute. value will be true or false. True if the letter is pressent in the word,
#false if its not. If not break parachute otherwise keep the same.
# draw_parachute() will draw the parachute in its current form
# parachute_broken() returns True if it's completely broken

class Parachute:

    def __init__(self):
        self._parachute = ['  _____', ' /_____\ ', ' \     /', '  \   /', '    0', '   /|\ ', '   / \ ']

    def break_parachute(self, value):
        if value == False:
            self._parachute = self._parachute.pop(0)

    def draw_parachute(self):
        for i in self._parachute:
            part = i
            print(part)

    def parachute_broken(self):
        return self._parachute == []