import random

def get_random_word(filename="resources/wordlist.txt"):
    with open(filename, "r") as file:
        words = file.read().splitlines()
    return random.choice(words).lower()