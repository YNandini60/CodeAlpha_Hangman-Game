import random
# ASCII hangman stages
HANGMAN_PICS = [
    """
     -----
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

def play_hangman():
    words = ["python", "apple", "banana", "computer", "school"]
    
   
    word = random.choice(words)
    guessed = ["_"] * len(word)  
    guessed_letters = []  
    attempts = 6  
    wrong_guesses = 0

    print("\n Welcome to Hangman!")
    print(HANGMAN_PICS[0])
    print("Guess the word:", " ".join(guessed))

    while attempts > 0 and "_" in guessed:
        guess = input("Enter a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print(" Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(" You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(" Good guess!")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
        else:
            wrong_guesses += 1
            attempts -= 1
            print(f" Wrong guess! Attempts left: {attempts}")

    
        print(HANGMAN_PICS[wrong_guesses])
        print("Word:", " ".join(guessed))
        print("Guessed letters:", ", ".join(guessed_letters))

    
    if "_" not in guessed:
        print(" Congratulations! You guessed the word:", word)
    else:
        print(" Game Over! The word was:", word)


def hangman():
    while True:
        play_hangman()
        again = input("\n Do you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("a Thanks for playing Hangman! Goodbye!")
            break


# Run the game
if __name__ == "__main__":
    hangman()
