import random
from words import listn

def choose_word():
    return random.choice(listn)

def display_word(word, guessed_letters):
    display = ""
    for i in word:
        if i in guessed_letters:
            display += i
        else:
            display += "_"
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 5

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while True:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("Incorrect!")
            print(f"Attempts left: {attempts}")
            if attempts == 0:
                print("You lose! The word was:", word)
                break
        else:
            print("Correct!")

        display = display_word(word, guessed_letters)
        print(display)

        if "_" not in display:
            print("Congratulations! You've won!")
            break

hangman()
