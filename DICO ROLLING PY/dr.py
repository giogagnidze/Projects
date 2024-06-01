import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Rolling Game!")
    print("You will compete against the computer to see who rolls the higher number.")

    while True:
        input("Press Enter to roll the dice: ")
        user_roll = roll_dice()
        computer_roll = roll_dice()

        print("You rolled:", user_roll)
        print("Computer rolled:", computer_roll)

        if user_roll > computer_roll:
            print("Congratulations! You win!")
        elif user_roll < computer_roll:
            print("Sorry, the computer wins.")
        else:
            print("It's a tie!")

        play_again = input("Do you want to play again? (y/n): ")
        if play_again != "y":
            print("Thanks for playing!")
            break
main()