# Python script for kinds of players

# Dependencies
import random 
import math

# SuperPlayer - GLOBAL
class SuperPlayer():
    def __init__(self, chosenLetter):
        self.chosenLetter = chosenLetter
        # Passing in handleTurn function for all players
        def handleTurn(self, ticTac):
            pass

# HumanPlayer - CHILD
class HumanPlayer(SuperPlayer):
    # Being "X" or "O"
    def __init__(self, chosenLetter):
        # Passing in SuperPlayer characteristics
        super().__init__(chosenLetter)

    # Because HumanPlayer, verifying if is a valid_move
    def handleTurn(self, ticTac):
      valid_move = False
      value = None
      while not valid_move:
          position = input(self.chosenLetter + "\"  turn. Input move (0-9): ")
          try:
              value = int(position)
              if value not in ticTac.available_moves():
                  raise ValueError
              valid_move = True
          except ValueError:
              print('Invalid position. Try again.')
      return value

# NormalComputer - CHILD
class NormalComputer(SuperPlayer):
    # Being "X" or "O"
    def __init__(self, chosenLetter):
        # Passing in SuperPlayer characteristics
        super().__init__(chosenLetter)

    def handleTurn(self, ticTac):
        position = random.choice(ticTac.available_moves())
        return position 

# AiComputer - CHILD
class AiComputer(SuperPlayer):
    # Being "X" or "O"
    def __init__(self, chosenLetter):
        # Passing in SuperPlayer characteristics
        super().__init__(chosenLetter)

    def handleTurn(self, ticTac):
        # If game has all 9 available positions
        if len (ticTac.available_moves()) == 9:
            position = random.choice(ticTac.available_moves())

        # If some positions are taken, minimax function comes into action
        else:
            position = self.MiniMaxFunction(ticTac, self.chosenLetter)['position']
        return position

    # Minimax Function
    def MiniMaxFunction(self, gameProgress, currentPlayer):
        # Providing a maximizedPlayer
        maximizedPlayer = self.chosenLetter
        # Creating FictionalPlayer to 'play' the game
        FictionalPlayer = "O" if currentPlayer == "X" else "X"

        # Utility Function
        # FictionalPlayer rotates between 'X' and 'O'
        if gameProgress.actualWinner == FictionalPlayer:
            # Returning a positive value
            return  {'position': None, 'score': 1 * (gameProgress.num_empty_positions() + 1)
            # Returning a negative value
            if FictionalPlayer == maximizedPlayer else -1 * (gameProgress.num_empty_positions() + 1)}
        # If there are no more positions left on the board (Draw): 0
        elif not gameProgress.empty_positions():
            return {'position': None, 'score': 0}

        # Maximizing score for maximizedPlayer
        if currentPlayer == maximizedPlayer:
            bestScore = {'position': None, 'score': -math.inf}
        # Minimizing score for other player
        else:
            bestScore = {'position': None, 'score': math.inf}
        
        # Simulating score with FictionalPlayer 
        for possible_move in gameProgress.available_moves():
            gameProgress.handleTurn(possible_move, currentPlayer)
            simulatedScore = self.MiniMaxFunction(gameProgress, FictionalPlayer)  

            # Undoing simulated game progress and looking for next optimal move
            gameProgress.board[possible_move] = ' '
            gameProgress.actualWinner = None
            simulatedScore['position'] = possible_move

            # Getting the optimal score
            if currentPlayer == maximizedPlayer:
                if simulatedScore['score'] > bestScore['score']:
                    bestScore = simulatedScore
            else:
                if simulatedScore['score'] < bestScore['score']:
                    bestScore = simulatedScore
        
        # Returning optimal score
        return bestScore