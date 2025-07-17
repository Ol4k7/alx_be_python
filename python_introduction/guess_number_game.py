import random

def play_game():
    secret_number = random.randint(1, 10)
    guess_count = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            guess_count += 1

            match guess:
                case _ if guess == secret_number:
                    print(f"Congratulations, you guessed it in {guess_count} tries!")
                    break
                case _ if guess > secret_number:
                    print("Oops, your guess is a bit high. Try again!")
                case _ if guess < secret_number:
                    print("Nope, your guess is a bit low. Give it another shot!")
        except ValueError:
            print("Invalid input, please enter a number.")

while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thank you for playing. Goodbye!")
        break
