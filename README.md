# 🎮 Hangman - Command-Line Game

[![License](https://img.shields.io/badge/license-MIT-blue.svg )](https://opensource.org/licenses/MIT )
[![Python](https://img.shields.io/badge/python-3.7%2B-blue )](https://www.python.org/ )
[![Build](https://img.shields.io/badge/build-passing-brightgreen )](#)
[![Maintenance](https://img.shields.io/badge/maintained-yes-green )](#)

A simple yet engaging **text-based Hangman game** built in Python for the command line. Challenge yourself to guess the hidden word one letter at a time — but watch out! Too many wrong guesses and the Hangman will meet his fate.

---

## 🧠 Features

- Random word selection from a built-in list or custom word file  
- ASCII art visuals to represent Hangman progress  
- User-friendly input system with validation  
- Win or lose detection with final word reveal  
- Clean, modular, and readable codebase  
- Easy to expand: Add difficulty levels, scoring, or themes  

---

## 📦 Technologies Used

- **Python 3** – For game logic and flow  
- **Command-line interface** – Fully playable in terminal or console  
- **ASCII art** – Visual representation of Hangman stages  

---

## ▶️ How to Play

1. Clone the repository

    ```bash
    git clone https://github.com/Soumyadeeps006/hangman-game
    ```

2. Run the game: 

    ```bash
    python run.py
    ```

3. Guess one letter at a time.

4. Reveal the full word before the Hangman is drawn completely.

5. Win by guessing the word or lose if you run out of tries.

---

## 🧪 Testing & Extensibility

This project is structured to support unit testing and future enhancements such as:
- Word categories (e.g., animals, movies, tech)
- Multiplayer or computer AI
- GUI version using Tkinter or Pygame
- Web version using Flask or Streamlit

---

## 🧪 How to Run the Tests

1. Make sure you're in the project root directory and run:

    ```bash
    python -m unittest tests/test_game.py -v
    ```

2. If you want to use pytest instead (faster and more readable output), install it:

    ```bash
    pip install pytest
    ```

3. Then run:

    ```bash
    python -m pytest tests/test_game.py -v
    ```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 💡 Contributing

Contributions are welcome! Whether you want to improve the code, add features, or fix bugs — feel free to open an issue or submit a pull request.

---

**Play. Learn. Build.**  
Perfect for beginners learning Python and game logic, or anyone looking to expand on a classic game. 🎯