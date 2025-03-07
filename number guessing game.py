import random
from replit import clear  # Assuming you have access to replit for the clear function
 # Assuming you have a logo defined in the art module
print("welcome to number GUESSINg game")

print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
# Function to set the number of attempts based on the difficulty level
def set_difficulty():
    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
        return 5
    else:
        return 0  # Return 0 if the input is invalid

    
    
def play_game():
    attempts = set_difficulty()
    if attempts == 0:
        print("Invalid difficulty level. Please choose 'easy' or 'hard'.")
        return
    number = random.randint(1, 100)
    print(f"You have {attempts} attempts remaining to guess the number.")
    while attempts > 0:
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"Congratulations! You guessed the number {number} correctly.")
            return
        elif guess < number:
            print("Too low.")
        else:
            print("Too high.")
        attempts -= 1
        if attempts > 0:
            print("Guess again.")
        print(f"You have {attempts} attempts remaining to guess the number.")
    print(f"Sorry, you've run out of attempts. The number was {number}.")

play_again = True
while play_again:
    play_game()
    play_again = input("Do you want to play again? Type 'yes' or 'no': ").lower() == "yes"
    clear()
    
                                
