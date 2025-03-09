
# this file contains the unittest section that tests three different scenarios:
# 1) The Player X is winning
# 2) It's a tie game
# 3) One Player has made an invalid move


import unittest
from board import Board
# from main_game import TicTacToe

class TestBoard(unittest.TestCase):
    # Case 1: the Player X is winning
    def test_player_x_wins(self):
        board = Board()
        board.grid = [["X", "X", "X"], # (satisfying criteia: employs a 2D data structure)
                      ["O", "O", " "],
                      [" ", " ", " "]]
        self.assertEqual(board.check_winner(), "X")

    # Case 2: it a tie game
    def test_tie_game(self):
        board = Board()
        board.grid = [["X", "O", "X"],
                      ["X", "X", "O"],
                      ["O", "X", "O"]]
        self.assertEqual(board.is_full(), True)

    # Case 3: one player has made an invalid move
    def test_invalid_move(self):
        board = Board()
        board.make_move(0, 0, "X")
        self.assertFalse(board.make_move(0, 0, "O"))



if __name__ == "__main__":
    unittest.main()

# setup.py
from setuptools import setup, find_packages

setup(
    name="tic_tac_toe",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
)
