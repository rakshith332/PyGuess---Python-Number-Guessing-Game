# Set the target number for the guessing game
target_number = 10

# Initialize the guess attempt counter
attempt_count = 0

# Set the maximum number of attempts allowed
max_attempts = 3

# Loop until the user guesses the correct number or exceeds the maximum attempts
while True:
    try:
        # Prompt the user to input a guess
        guess = int(input('Enter your guess: '))

        # Check if the guess matches the target number
        if guess == target_number:
            print("Congratulations! You've guessed the correct number. You won!")
            break
        else:
            # Increment the attempt count
            attempt_count += 1
            
            # Calculate the remaining attempts
            remaining_attempts = max_attempts - attempt_count
            
            # Check if the user has remaining attempts
            if attempt_count < max_attempts:
                print(f"Incorrect guess. You have {remaining_attempts} attempts remaining.")
            else:
                print("Sorry, you've reached the maximum number of attempts. Please try again later.")
                break
    except ValueError:
        # Handle invalid input (non-integer)
        print("Invalid input! Please enter a valid integer.")

