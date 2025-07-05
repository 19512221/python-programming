import random

def choose_word():
    words = ["apple", "brain", "crane", "drink", "eagle"]
    return random.choice(words)

def display_state(secret, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in secret)

def play_hangman():
    secret = choose_word()
    guessed = set()
    wrong = set()
    max_wrong = 6

    print("Welcome to Hangman!")
    print(f"You have up to {max_wrong} incorrect guesses. Good luck!")

    while True:
        print("\nWord:", display_state(secret, guessed))
        print(f"Wrong guesses ({len(wrong)}/{max_wrong}):", " ".join(sorted(wrong)))

        if set(secret) <= guessed:
            print(f"\n Congratulations! You guessed the word: **{secret}**")
            break

        if len(wrong) >= max_wrong:
            print(f"\n Game over! You've used all {max_wrong} guesses. The word was: **{secret}**")
            break

        guess = input("Guess a letter: ").lower().strip()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.")
            continue
        if guess in guessed or guess in wrong:
            print("You've already guessed that letter.")
            continue

        if guess in secret:
            print("Good one!")
            guessed.add(guess)
        else:
            print("Nope.")
            wrong.add(guess)

if __name__ == "__main__":
    play_hangman()

        