
# Libraries

import random
import turtle

turtle.hideturtle()
turtle.penup()
turtle.goto(0, 150)


secret_number = random.randint(1, 10)

guess_number = 0
while guess_number != secret_number:
    # guess_number = int(input("Guess a number between 1 and 10: "))
    guess_number = int(turtle.numinput("Casino Game", "Guess a number between 1 and 10", minval=1, maxval=10))

    turtle.clear()

    if guess_number == secret_number:
        turtle.write("You Won!", align="center", font=("Arial", 20, "bold"))
        break
    elif guess_number > secret_number:
        turtle.write("Too High!", align="center", font=("Arial", 20, "bold"))
    else:
        turtle.write("Too Low!", align="center", font=("Arial", 20, "bold"))
turtle.done()


