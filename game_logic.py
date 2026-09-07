import random
from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays current ASCII stage and word progress."""
    print(STAGES[mistakes])

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word: ", display_word)
    print("\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!\n")

    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)

        # Gewonnen-Prüfung
        if all(letter in guessed_letters for letter in secret_word):
            print("Congratulations! You saved the snowman!\n")
            return

        guess = input("Guess a letter: ").lower().strip()

        # Eingabevalidierung (Zusatzanforderung)
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!\n")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            mistakes += 1
            print("Wrong guess! The snowman is melting...\n")
        else:
            print("Good guess!\n")

    # Niederlage-Prüfung
    display_game_state(mistakes, secret_word, guessed_letters)
    print(f"Game Over! The snowman melted completely. The word was: {secret_word}\n")