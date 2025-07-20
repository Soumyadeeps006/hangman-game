import unittest
from hangman.words import get_random_word
from hangman.display import display_word

class TestHangmanGame(unittest.TestCase):

    def test_get_random_word_returns_string(self):
        word = get_random_word()
        self.assertIsInstance(word, str)
        self.assertGreater(len(word), 0)

    def test_get_random_word_is_lowercase(self):
        word = get_random_word()
        self.assertEqual(word, word.lower())

    def test_display_word_all_guessed(self):
        word = "apple"
        guessed_letters = set("apple")
        result = display_word(word, guessed_letters)
        self.assertEqual(result, "a p p l e")

    def test_display_word_no_guesses(self):
        word = "banana"
        guessed_letters = set()
        result = display_word(word, guessed_letters)
        self.assertEqual(result, "_ _ _ _ _ _")

    def test_display_word_partial_guesses(self):
        word = "cherry"
        guessed_letters = {'c', 'h', 'y'}
        result = display_word(word, guessed_letters)
        self.assertEqual(result, "c h _ _ _ y")

    def test_display_word_repeats(self):
        word = "pepper"
        guessed_letters = {'p'}
        result = display_word(word, guessed_letters)
        self.assertEqual(result, "p _ p p _ _")

if __name__ == '__main__':
    unittest.main()