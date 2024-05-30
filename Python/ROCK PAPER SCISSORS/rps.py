import random
# Rock Paper Scissors
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == 'rock':
        if computer_choice == 'scissors':
            return "You win!"
        else:
            return "Computer wins!"
    elif user_choice == 'paper':
        if computer_choice == 'rock':
            return "You win!"
        else:
            return "Computer wins!"
    elif user_choice == 'scissors':
        if computer_choice == 'paper':
            return "You win!"
        else:
            return "Computer wins!"

def play_game():
    print("Let's play Rock, Paper, Scissors!")
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    
    print(f"You chose {user_choice}.")
    print(f"The computer chose {computer_choice}.")
    print(determine_winner(user_choice, computer_choice))

play_game()
