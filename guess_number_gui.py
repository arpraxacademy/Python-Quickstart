"""
Project 2 (Bonus): Casino Game (GUI Version)
Part of the 'Python Fast Track' Bootcamp by Arprax Academy.

📺 Watch the Tutorial for this Script: [LINK_TO_CASINO_VIDEO]
▶️ Full Course Playlist: https://youtube.com/playlist?list=PL7kitcmP3RiO724GV3Fmb1MHEp0g9RYnJ&si=ozyOr1brpt0lUbEH

Description:
The same logic as the previous game, but visualized using Python's 
built-in 'turtle' library. This simulates building a visual app.
"""

# Libraries
import random
import turtle

# Setup the Visuals
# Hide the turtle icon so we just see text
turtle.hideturtle()
turtle.penup()
turtle.goto(0, 150)  # Move text to the top of the screen

# Backend Logic
secret_number = random.randint(1, 10)
guess_number = 0

# The Game Loop
while guess_number != secret_number:

    # Instead of console input, we use a Popup Box
    guess_number = int(turtle.numinput("Casino Game", "Guess a number between 1 and 10", minval=1, maxval=10))

    # Clear the previous "Too High" message
    turtle.clear()

    # Visual Output
    if guess_number == secret_number:
        turtle.write("You Won!", align="center", font=("Arial", 20, "bold"))
        break
    elif guess_number > secret_number:
        turtle.write("Too High!", align="center", font=("Arial", 20, "bold"))
    else:
        turtle.write("Too Low!", align="center", font=("Arial", 20, "bold"))

# Keep window open until user closes it
turtle.done()