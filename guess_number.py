"""
Project 2: Casino Guessing Game (Logic Version)
Part of the 'Python Fast Track' Bootcamp by Arprax Academy.

📺 Watch the Tutorial for this Script: https://youtu.be/pje1Z49zj-8
▶️ Full Course Playlist: https://youtube.com/playlist?list=PL7kitcmP3RiO724GV3Fmb1MHEp0g9RYnJ&si=ozyOr1brpt0lUbEH

Description:
The computer picks a random number, and you have to guess it.
This teaches:
- Importing Libraries (random)
- The 'While' Loop (Running code forever until a condition is met)
- Conditional Logic (If / Elif / Else)
"""

# Libraries
import random

# Generate a random integer between 1 and 10 (inclusive)
secret_number = random.randint(1, 10)

# Initialize the variable so the while loop runs at least once
guess_number = 0

# The Game Loop
# This will run forever until guess_number equals secret_number
while guess_number != secret_number:

    # Get input and cast to integer immediately
    guess_number = int(input("Guess a number between 1 and 10: "))

    # Check the guess
    if guess_number == secret_number:
        print("You Won!")
        break  # Stops the loop immediately
    elif guess_number > secret_number:
        print("Too High!")
    else:
        print("Too Low!")