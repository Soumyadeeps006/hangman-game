from hangman.words import get_random_word
from hangman.display import display_hangman, display_word

class HangmanGame:
    def __init__(self):
        self.word = get_random_word()
        self.guessed_letters = set()
        self.tries = 6
        self.win = False

    def start(self):
        print("🎮 Welcome to Hangman!")
        while self.tries > 0 and not self.win:
            print(display_hangman(self.tries))
            print(display_word(self.word, self.guessed_letters))
            guess = input("Enter a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("⚠️ Please enter a single letter.")
                continue

            if guess in self.guessed_letters:
                print("🔁 Already guessed that letter.")
                continue

            self.guessed_letters.add(guess)

            if guess in self.word:
                print("✅ Good guess!")
                if all(letter in self.guessed_letters for letter in self.word):
                    self.win = True
            else:
                print("❌ Wrong guess!")
                self.tries -= 1

        if self.win:
            print(f"🎉 Congratulations! You guessed the word: {self.word}")
        else:
            print(display_hangman(self.tries))
            print(f"💀 Game Over! The word was: {self.word}")