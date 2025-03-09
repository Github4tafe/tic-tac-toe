

# this file create the TicTacToe module that contains the main game play functions,
# including switch_player(), play(), and get_move().


# import Board modular from board.py (satisfying criteia: one import statement of your modules)
from board import Board


# Create the TicTacToe class (satisfying criteia: two of the two classes)
class TicTacToe:
    def __init__(self):
        self.board = Board()
        self.players = ["X", "O"]
        self.current_player = 0

    def switch_player(self):
        self.current_player = 1 - self.current_player

    # Method of the main game loop, which is the key function responsible for running the Tic-Tac-Toe
    def play(self):
        while True:
            self.board.display()
            row, col = self.get_move()
            if self.board.make_move(row, col, self.players[self.current_player]):
                winner = self.board.check_winner()
                if winner:
                    self.board.display()
                    print(f"Player {winner} wins!")
                    break
                if self.board.is_full():
                    print("It's a tie!")
                    break
                self.switch_player()
            else:
                print("Invalid move, try again.")

    # Method of record players move and ensure the move is valid, otherwise prompt error message.
    def get_move(self):
        while True:
            move = input(f"Player {self.players[self.current_player]} (row col): ").split()
            if len(move) == 2 and move[0].isdigit() and move[1].isdigit():
                row, col = map(int, move)
                if 0 <= row < 3 and 0 <= col < 3:
                    return row, col
            print("Invalid input, try again.")