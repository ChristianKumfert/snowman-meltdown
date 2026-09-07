import random

# 1. ASCII-Art für die Schmelzstufen (0 Fehler bis 5 Fehler)
SNOWMAN_STAGES = [
    # 0 Fehler: Vollständiger Schneemann
    """
     ___ 
    /___\\
    (o o)
    ( : )
    ( : )
    """,
    # 1 Fehler: Hut schmilzt
    """

    /___\\
    (o o)
    ( : )
    ( : )
    """,
    # 2 Fehler: Kopf ohne Hut
    """


    (o o)
    ( : )
    ( : )
    """,
    # 3 Fehler: Oberer Körper schmilzt
    """



    ( : )
    ( : )
    """,
    # 4 Fehler: Nur noch die Basis
    """




    ( : )
    """,
    # 5 Fehler: Komplett geschmolzen (Game Over)
    """




    ( . )
    """
]

# 2. Wörterliste zur Auswahl
WORDS = ["python", "codio", "github", "program", "snowman"]


def display_game_state(snowman_stages, wrong_guesses, secret_word, guessed_letters):
    """Zeigt den aktuellen Schneemann und das Wort mit geratenen Buchstaben an."""
    print(snowman_stages[wrong_guesses])

    # Ersetzt ungeratene Buchstaben durch Unterstriche '_'
    display_word = [letter if letter in guessed_letters else "_" for letter in secret_word]
    print("Word: " + " ".join(display_word))
    print()


def main():
    secret_word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong_guesses = len(SNOWMAN_STAGES) - 1

    print("Welcome to Snowman Meltdown!\n")

    # Spielschleife läuft, solange der Schneemann nicht geschmolzen ist
    while wrong_guesses < max_wrong_guesses:
        display_game_state(SNOWMAN_STAGES, wrong_guesses, secret_word, guessed_letters)

        # Prüfen, ob alle Buchstaben des Wortes geraten wurden (Sieg)
        if all(letter in guessed_letters for letter in secret_word):
            print("Congratulations! You saved the snowman!")
            break

        guess = input("Guess a letter: ").lower().strip()

        # Eingabevalidierung
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!\n")
            continue

        guessed_letters.add(guess)

        # Treffer oder Fehlschlag auswerten
        if guess not in secret_word:
            wrong_guesses += 1
            print("Wrong guess! The snowman is melting...\n")
        else:
            print("Good guess!\n")

    # Spielende durch Niederlage
    if wrong_guesses == max_wrong_guesses:
        display_game_state(SNOWMAN_STAGES, wrong_guesses, secret_word, guessed_letters)
        print(f"Game Over! The snowman melted completely. The word was: {secret_word}")


if __name__ == "__main__":
    main()