# test_game.py

import unittest
from game import guess_number

class TestGame(unittest.TestCase):
    def test_guess_number(self):
        # Test whether the guess_number function returns without errors
        # No easy way to test random number generation, so this is a basic test
        guess_number()

if __name__ == "__main__":
    unittest.main()

