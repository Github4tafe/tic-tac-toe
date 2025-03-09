
# this file create the Board module that construct and display the empty board, and a few other board relevent functions,
# including is_full(), make_move(), and check_winner().

# Create the Board class (satisfying criteia: one of the two classes)
class Board:
    def __init__(self):
        self.empty = " "
        self.grid = [[self.empty for _ in range(3)] for _ in range(3)]

    # Method that displays the empty board
    def display(self):
        for row in self.grid:
            print(" | ".join(row))
            print("-" * 9)

    # Method that checks if the board is empty or not (required for defining a tie game)
    def is_full(self):
        return all(cell != self.empty for row in self.grid for cell in row)


    # Method that updates the board and ensure the cell is empty for the player,
    # otherwise it returns False if the cell is occupied
    def make_move(self, row, col, player):
        if self.grid[row][col] == self.empty:
            self.grid[row][col] = player
            return True
        return False

    # Method that concludes the game, either defines the winner or a tie game.
    def check_winner(self):
        for row in self.grid:
            if row[0] == row[1] == row[2] != self.empty:
                return row[0]
        for col in range(3):
            if self.grid[0][col] == self.grid[1][col] == self.grid[2][col] != self.empty:
                return self.grid[0][col]
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != self.empty:
            return self.grid[0][0]
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != self.empty:
            return self.grid[0][2]
        return None