# Python script for game rules

# Dependencies
import math
import time
from all_players import AiComputer, HumanPlayer, NormalComputer

# Main function
class PlayGame():
    def __init__(self):
        self.board = self.boardDesign()
        self.actualWinner = None

    @staticmethod
    def boardDesign():
        # -  -  -
        return [" " for _ in range(9)]

    def printBoard(self):
        # |  |  |  |
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def printBoardNumbers():
        # 0 | 1 | 2
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    # If there's an available position, assign the current player's chosenLetter
    def handleTurn(self, position, chosenLetter):
        if self.board[position] == " ":
            self.board[position] = chosenLetter
            if self.winningPlayer(position, chosenLetter):
                self.actualWinner = chosenLetter
            return True
        return False

    # Defining winning conditions
    def winningPlayer(self, position, chosenLetter):
        # check the row
        row_ind = math.floor(position / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        # print('row', row)
        if all([s == chosenLetter for s in row]):
            return True
        col_ind = position % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
        if all([s == chosenLetter for s in column]):
            return True
        if position % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
            if all([s == chosenLetter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == chosenLetter for s in diagonal2]):
                return True
        return False  

    # Empty positions available for utility function
    def empty_positions(self):
        return ' ' in self.board
    
    # Count number of empty positions available for utility function
    def num_empty_positions(self):
        return self.board.count(' ')

    # Returning position number of empty spots
    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]

# Assigning turns to X and O and stating actualWinner
def GameInitiation(ticTac, Xplayer, Oplayer, StartGame=True):
    if StartGame:
        ticTac.printBoardNumbers()

    # X is always the first to play
    chosenLetter = "X"
    while ticTac.empty_positions():
        if chosenLetter == "O":
            position = Oplayer.handleTurn(ticTac)
        else:
            position = Xplayer.handleTurn(ticTac)
        if ticTac.handleTurn(position, chosenLetter):
            # Printing into terminal position taken
            if StartGame:
                print("Assigned position {} to ".format(position) + chosenLetter)
                ticTac.printBoard()
                print("")
            # Winner
            if ticTac.actualWinner:
                if StartGame:
                    print(chosenLetter + " wins the game :D !!")
                return chosenLetter
            chosenLetter = "O" if chosenLetter == "X" else "X"
        # Timelapse
        time.sleep(.30)
    # If no more empty positions
    if StartGame:
        print("Draw! No one wins")

# Start the game- select players
# AiComputer, HumanPlayer, NormalComputer
if __name__ == '__main__':
    Xplayer = AiComputer("X")
    Oplayer = HumanPlayer("O")
    g = PlayGame()
    GameInitiation(g, Xplayer, Oplayer, StartGame=True)
