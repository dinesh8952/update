import unittest
from game import guess_number

class TestGame(unittest.TestCase):
    def test_guess_number_correct_guess(self):
        # Test correct guess
        secret_number = 5
        user_guess = 5
        result = guess_number(secret_number, user_guess)
        self.assertTrue(result)
    
    def test_guess_number_incorrect_guess(self):
        # Test incorrect guess
        secret_number = 5
        user_guess = 10
        result = guess_number(secret_number, user_guess)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()


