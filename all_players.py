## ALL_PLAYERS.PY

# IMPORTING DEPENDENCIES
import math
import random 

# PLAYER - GLOBAL CLASS
class SuperPlayer():
    def __init__(self, chosenLetter):
        self.chosenLetter = chosenLetter

        def make_move(self, ticTac):
            pass

# HUMAN PLAYER - CHILD CLASS
class HumanPlayer(SuperPlayer):
    def __init__(self, chosenLetter): # self being 'X' or 'O'
        super().__init__(chosenLetter) # calling SuperPlayer functionality

        def make_move(self, ticTac):
            valid_move = False
            value = None
            while not valid_move:
                position = input(self.chosenLetter + '\'s turn. Input move (0-9): ')
                try:
                    value = int(position)
                    if value not in ticTac.available_moves():
                        raise ValueError
                    valid_move = True
                except ValueError:
                    print('Invalid position. Try again.')
            return value


# NORMAL COMPUTER - CHILD CLASS
class NormalComputer(SuperPlayer):
    def __init__(self, chosenLetter):
        super().__init__(chosenLetter)

    def make_move(self, ticTac):
        position = random.choice(ticTac.available_moves())
        return position 

# AI COMPUTER - CHILD CLASS
class AiComputer(SuperPlayer):
    def __init__(self, chosenLetter):
        super().__init__(chosenLetter)

    def make_move(self, ticTac):
        if len (ticTac.available_moves()) == 9:
            position = random.choice(ticTac.available_moves())
        else:
            position = self.MiniMax(ticTac, self.chosenLetter)['position']
        return position

        # MINIMAX FUNCTION



