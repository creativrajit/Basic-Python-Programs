'''
    This program generates a random number from 1 to 50 and ask user to guess
'''
import random

# Let's welcome player
print("Welcome to a game created by Swopna \n")

# Generate a random number
target_number = random.randrange(1, 51)

# Initialize variables needed
guessed_it = False
num_of_guesses = 0

# Loop until player guesses right or game over
while(num_of_guesses < 5) or (guessed_it):

    # Ask for user to guess input
    user_input = eval(input("Please guess a number: "))

    # Check if user guess matches target
    if (user_input == target_number):
        guessed_it = True
        print("Hurray! you guessed the right number")
        break
    elif (user_input < target_number):
        print("Guess higher nnumber")
    elif (user_input > target_number):
        print("Guess lower number")
    else:

        print("Please enter a valid integer")

    num_of_guesses += 1

# If player lost
if not(guessed_it):
    print("Sorry you lost. \n Correct number was ", target_number)



