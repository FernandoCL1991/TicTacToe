# PLAYER - GLOBAL CLASS
# HUMAN PLAYER - CHILD CLASS
# NORMAL COMPUTER - CHILD CLASS
# AI COMPUTER - CHILD CLASS

# PLAYER - GLOBAL CLASS
class Player():
    def __init__(self, chosenLetter):
        self.chosenLetter = chosenLetter

# HUMAN PLAYER - CHILD CLASS
class HumanPlayer(Player):
    def __init__(self, chosenLetter):
        super()__init__(chosenLetter)

# NORMAL COMPUTER - CHILD CLASS
class NormalComputer(Player):
    def __init__(self, chosenLetter):
        super()__init__(chosenLetter)

# AI COMPUTER - CHILD CLASS - MINIMAX
class AiComputer(Player):
    def __init__(self, chosenLetter):
        super()__init__(chosenLetter)