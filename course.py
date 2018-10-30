########### Seyhan Van Khan
########### Turtle Race
########### Race turtles in a multiple difficulty racecourse while avoiding obstacles
########### September 2018
""" Functions:
        PlaceCoin(coin, colour, shape) - places a coin randomly around track
        introduceturt(turtle, turtle_name, starting_x, starting_y) - introduces turtle to user on screen & places at starting position
        setupturtle(turtle, turtle_name, colour, shape, starting_x_pos, starting_y_pos) - Initalises a new turtle in a certain position, colour, shape
        moveturtle(turtle, position, xleg, yleg) - Moves opponents randomly & simultaneously around racecourse according to given distances & turning points
        resetturtle(turtle) - If hit by obstacle, turtle resets to starting position
        outofbounds(turtle) - Checks if turtle is outside racecourse boundary
        reachedfinish(turtle) - Checks if turtle has reached the finish line
"""
from random import choice
from turtle import *


def PlaceCoin(coin, colour="red", shape="circle"):
    # Places a circular, red coin (obstacle) in a random part of race track
    coin.ht()
    coin.pu()
    # Randomly picks a section of track to put the coin in
    section = randint(1,2)
    if section == 1:
        # Places coin in a random position within the section boundaries
        coin.goto(randint(-280, 180), randint(210, 250))
        coin.seth(90)
    else:
        coin.goto(randint(210, 280), randint(-80, 180))
        coin.seth(0)
    coin.shape(shape)
    coin.color(colour)
    coin.st()


def introduceturt(player, name, x, y):
    # Places turtle in starting position
    # Prints its name on the screen
    player.st()
    player.goto(x, y)
    goto(x - 40, y)
    color("black")
    write(name, align = 'center', font = ("Comic Sans MS", 20, "normal"))

    # Each turtle does a full spin in a random direction to start off with
    if randint(1, 2) == 1:
        player.right(360)
    else:
        player.left(360)


def setupturtle(player, name, colour, shape, x, y):
    # Gives turtle attributes of given colour & shape
    # Initalises turtle in certain position (using introduceturt() function)
    player.shape(shape)
    player.color(colour)
    player.pu()
    introduceturt(player, name, x, y)
    return player.pos()


def moveturtle(turtle, position, xleg, yleg):
    # Moves each turtle by short random amount
    # The turtle ends up moving in a random direction at a random speed (within limits)
    # If turtle has finished a leg based on its coordinates
    ### It turns right
    if outofbounds(turtle):
        return True
    else:
        # Turtle still moves forward but direction & speed slightly changes every time
        turtle.forward(randint(3, 5))
        turtle.right(randint(-2, 2))
        turtle.forward(randint(3, 5))

        if (turtle.heading() < 15 or turtle.heading() > 345) and turtle.xcor() > position[0] + xleg:
            # If turtle is heading generally East & is past the distance required to turn right to stay on track
            turtle.right(92)
            turtle.fd(1)
            turtle.left(2)

        if turtle.heading() > 259 and turtle.ycor() < position[1] - yleg:
            # If turtle is heading generally South & is past the distance required to turn right to stay on track
            turtle.right(88)
            turtle.fd(1)
            turtle.right(2)

        return False


def resetturtle(turtle):
    turtle.seth(0)
    turtle.goto(-360, 225)


def outofbounds(turtle):
    # Checks if turtle is outside of the racecourse boundary
    ### If so, returns true
    x = turtle.xcor()
    y = turtle.ycor()
    if (
       x > 280 or
       x < -390 or
       y > 280 or
       y < -150 or
       x < 200 and y < 200 and y > -80 or
        x < -240 and y < -80
       ):
        return True
    else:
        return False


def reachedfinish(turtle):
    # Checks if turtle is within the finish line boundaries
    return True if turtle.xcor() < -230 and turtle.ycor() < -79 else False
