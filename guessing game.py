import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")
    
    # Randomly select a number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    # Initialize the number of attempts
    attempts = 0
    
    while True:
        # Increment the attempt counter
        attempts += 1
        
        # Ask the player for a guess
        guess = int(input("Enter your guess: "))
        
        # Check if the guess is correct
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

if __name__ == "__main__":
    guessing_game() 