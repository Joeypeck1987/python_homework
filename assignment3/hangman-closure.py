# Task 4: Closure Practice


def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        letter = letter.lower()

        if letter not in guesses:
            guesses.append(letter)

        displayed_word = "".join(
            character if character.lower() in guesses else "_"
            for character in secret_word
        )

        print(displayed_word)

        return displayed_word == secret_word

    return hangman_closure


secret_word = input("Enter the secret word: ").lower()
hangman_game = make_hangman(secret_word)

word_is_guessed = False

while not word_is_guessed:
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1:
        print("Please enter one letter.")
        continue

    word_is_guessed = hangman_game(guess)

print("You guessed the word!")