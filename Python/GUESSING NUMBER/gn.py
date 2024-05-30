import random
def guess_number(min_num, max_num):
    secret_number = random.randint(min_num, max_num)
    attempts = 0
    while True:
        guess = int(input(f"Guess the number between {min_num} and {max_num}: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} correctly in {attempts} attempts.")
            break
    return attempts
def main():
    print("Welcome to the Number Guessing Game!")
    min_num = int(input("Enter the minimum number of the range: "))
    max_num = int(input("Enter the maximum number of the range: "))
    attempts = guess_number(min_num, max_num)
    print(f"Number of attempts: {attempts}")
main()