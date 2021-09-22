# BOARD PRINTED
# BOARD WITH NUMBERS DISPLAYED
# 

class PlayGame():
    def __init__(self):
        self.board = self.boardDesign()
        self.actualWinner = None

    @staticmethod
    def boardDesign():
        # -  -  -
        return ["-" for _ in range(9)]

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

    def handleTurn(self, position, letter):
        if self.board[position] == "-":
            self.board[position] = letter
            if self.winningPlayer(position, letter):
                self.actualWinner = letter
            return True
        return False ###  <<< --- REVISAR POR QUÉ FALSE
    
    def winningPlayer(self, position, letter):
        # Winning Row
        winning_row1 = position[0] == position[1] == position[2] != "-"
        winning_row2 = position[3] == position[4] == position[5] != "-"
        winning_row3 = position[6] == position[7] == position[8] != "-"
        if all([letter == letter in winning_row1, winning_row2, winning_row3]):
            return True
        if winning_row1:
            return position[0]
        if winning_row2:
            return position[3]
        if winning_row3:
            return position[6]
        # Winning Column
        winning_col1 = position[0] == position[3] == position[6] != "-"
        winning_col2 = position[1] == position[4] == position[7] != "-"
        winning_col3 = position[2] == position[5] == position[8] != "-"
        if all([letter == letter in winning_col1, winning_col2, winning_col3]):
            return True
        if winning_col1:
            return position[0]
        if winning_col2:
            return position[1]
        if winning_col3:
            return position[2]
        # Winning Diagonal
        winning_diagonal1 = position[0] == position[4] == position[8] != "-"
        winning_diagonal2 = position[6] == position[4] == position[2] != "-"
        if all([letter == letter in winning_diagonal1, winning_diagonal2]):
            return True
        if winning_diagonal1:
            return position[0]
        if winning_diagonal2:
            return position[6]

    def empty_squares(self): ###---> REVISAR!
        return ' ' in self.board

    def num_empty_squares(self): ###---> REVISAR!
        return self.board.count(' ')

    def available_moves(self): ###---> REVISAR!
        return [i for i, x in enumerate(self.board) if x == " "]

def GameInitiation(ticTac, Xplayer, Oplayer, StartGame = True):

### PASAR A all_players