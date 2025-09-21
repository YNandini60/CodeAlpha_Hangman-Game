# CodeAlpha_Hangman-Game Task1

This Hangman game is developed as CodeAlpha Internship Task 1. It’s a simple text-based Python game where players guess a hidden word one letter at a time. It includes ASCII art for wrong guesses, tracks attempts, prevents duplicate guesses, and allows multiple rounds with replay support.

# Hangman Game   
**CodeAlpha Internship – Task 1**

##  Overview
This project is a **text-based Hangman game**  with built in Python   
The game challenges players to guess a hidden word by entering one letter at a time. If the guess is correct, the letter is revealed in the word. If incorrect, a part of the hangman drawing is added. The game ends when the player either guesses the full word or runs out of attempts.

##  Features
- Uses a predefined list of 5 words (`python, apple, banana, computer, school`).
- Maximum of **6 incorrect guesses** allowed.
- **ASCII art stages** for the hangman drawing.
- Tracks guessed letters and prevents duplicate entries.
- Input validation (only single alphabetic characters allowed).
- **Replay option** to play multiple rounds without restarting the program.
- Win/lose messages for better user experience.

##  Technologies Used
- **Python 3**
- **Random module** (for word selection)
- Basic **string and list operations**
- **While loops** and **if-else logic**

##  How to Run
1. Install Python (version 3.6 or above recommended).
2. Save the file as `hangman.py`.
3. Run the program in the terminal:
   ```bash
   python hangman.py
   
##  Example Gameplay
```
Welcome to Hangman!
Guess the word: _ _ _ _ _ _

Enter a letter: a
Wrong guess! Attempts left: 5
  -----
  |   |
  O   |
      |
      |
      |
=========
Word: _ _ _ _ _ _
Guessed letters: a

```
##  Hangman Stages

```
Stage 0:
  -----
  |   |
      |
      |
      |
      |
=========

Stage 1:
  -----
  |   |
  O   |
      |
      |
      |
=========

Stage 2:
  -----
  |   |
  O   |
  |   |
      |
      |
=========

Stage 3:
  -----
  |   |
  O   |
 /|   |
      |
      |
=========

Stage 4:
  -----
  |   |
  O   |
 /|\  |
      |
      |
=========

Stage 5:
  -----
  |   |
  O   |
 /|\  |
 /    |
      |
=========

Stage 6:
  -----
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
```
##  Learning Outcomes

* Use of **loops, conditionals, and lists** in Python.
* Handling **user input and validation**.
* Managing **game state** and replay logic.
* Improving code readability and structure.

 **Author**: \[Srinidhi]
 **Internship**: CodeAlpha Internship
 **Task**: Task 1 – Hangman Game
