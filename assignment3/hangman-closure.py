# Task 4: Closure Practice


def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)

        displayed_word = ""

        for character in secret_word:
            if character in guesses:
                displayed_word += character
            else:
                displayed_word += "_"

        print(displayed_word)

        return displayed_word == secret_word

    return hangman_closure


secret_word = input("Enter the secret word: ").lower()

game = make_hangman(secret_word)

word_guessed = False

while not word_guessed:
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1:
        print("Please enter one letter.")
        continue

    word_guessed = game(guess)

print("You guessed the word!")