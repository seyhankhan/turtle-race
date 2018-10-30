########### Seyhan Van Khan
########### Turtle Race
########### Race turtles in a multiple difficulty racecourse while avoiding obstacles
########### September 2018

from time import sleep

from turtle import *
from course import *
import login


########################## Welcoming User ##########################


# Creates a turtle to write an intro message and removes it after 1 second
speed(0)
hideturtle()
penup()
goto(0,0)
write("Welcome to Turtle Race", align = 'center', font = ("Arial", 40, "normal"))
sleep(1)
reset()
ht()
pu()


###################### Customising Characters ######################


# Opens the "menu" function from module login
# User can specify gamemode (singleplayer, multiplayer) & look at controls
# Coins are the obstacles
num_player, framedelay, no_coins = login.menu()

# Creates a turtle for player
player1 = Turtle()
player1.resizemode("user")
player1.shapesize(1.3, 1.3, 1.3)
player1.hideturtle()

print("PLAYER 1:" if num_player == 2 else "")
# Opens function attribute from module login
# Creates attributes for the player's turtle
name1 = login.attribute(player1)

if num_player == 2:
    # Creates a turtle for player
    print("PLAYER 2:")
    player2 = Turtle()
    player2.resizemode("user")
    player2.shapesize(1.3, 1.3, 1.3)
    player2.hideturtle()
    # Opens function attribute from module login
    # Creates attributes for the player's turtle
    name2 = login.attribute(player2)


########################## Creating track ##########################


# Creates a green box as a "finish line"
ht()
speed(0)
pu()
color("green")
pensize(1)
fillcolor("green")
begin_fill()
goto(-240, -80)
pd()
goto(-240, -150)
goto(-298, -150)
goto(-298, -80)
goto(-240, -80)
end_fill()

# Creates racecourse shaped like a U with the colour grey (unless otherwise stated)
pu()
color("grey")
goto(-390, 280)
pd()
pensize(7)
goto(280, 280)
goto(280, -150)
goto(-300, -150)
goto(-300, -80)
goto(200, -80)
goto(200, 200)
goto(-390, 200)
goto(-390, 275)
pu()

coin_proximity = int(60) # Minimum distance between coins
coin1 = Turtle()
coin2 = Turtle()
coinlist = [coin1, coin2]
# Randomly places the coins around the track
# Ensures coins are placed far apart from each other
PlaceCoin(coin1)
PlaceCoin(coin2)
while coin2.distance(coin1) < coin_proximity:
    # Keep placing coin2 somewhere randomly until coin2 isn't too close to coin1
    PlaceCoin(coin2)

if no_coins == 3:
    coin3 = Turtle()
    coinlist.append(coin3)
    PlaceCoin(coin3)
    while coin3.distance(coin2) < coin_proximity and coin3.distance(coin1) < coin_proximity:
        PlaceCoin(coin3)


############################# Keybinds #############################


# Keybinds the arrow keys to control the player turtle
# Starting speed for player
playerspeed1 = 1
screen1 = Screen()
screen1.tracer(framedelay)
# Functions define what occurs when the key is pressed
def upspeed1():
    # Player accelerates up to speed max of 8
    global playerspeed1
    playerspeed1 = (playerspeed1 + 0.5) if playerspeed1 < 8 else 8

def downspeed1():
    # Player decelerates down to min speed of 0
    global playerspeed1
    playerspeed1 = (playerspeed1 - 1) if playerspeed1 > 0 else 0

# User controls turtle with arrow keys
player1.pu()
screen1.listen()
# Functions of up, down, left and right are binded to arrow keys
screen1.onkey(upspeed1, 'Up' )
screen1.onkey(downspeed1, 'Down' )
screen1.onkey(lambda: player1.left(30), 'Left' )
screen1.onkey(lambda: player1.right(30), 'Right' )

if num_player == 2:
    playerspeed2 = 1

    def upspeed2():
        # Player accelerates up to speed max of 8
        global playerspeed2
        playerspeed2 = (playerspeed2 + 0.5) if playerspeed2 < 8 else 8

    def downspeed2():
        # Player decelerates down to min speed of 0
        global playerspeed2
        playerspeed2 = (playerspeed2 - 1) if playerspeed2 > 0 else 0

    player2.pu()
    screen1.listen()
    # Functions of up, down, left and right are binded to WASD keys
    screen1.onkey(upspeed2, 'w')
    screen1.onkey(downspeed2, 's')
    screen1.onkey(lambda: player2.left(30), 'a' )
    screen1.onkey(lambda: player2.right(30), 'd' )


########################## Placing racers ##########################


# The distances the computer controlled turtles must travel around course = distance1 & distance2
distance1 = 600
distance2 = 380
# Creates 2 opponents
adam = Turtle()
bob = Turtle()
turtlelist = [player1, adam, bob]
if num_player == 2:
    turtlelist.append(player2)

color("black")
starting_pos_A = setupturtle(adam, "ADAM", "Purple", "arrow", -360, 270)
starting_pos_B = setupturtle(bob, "BOB", "Blue", "turtle", -360, 250)
introduceturt(player1, name1.upper(), -360, 225)
if num_player == 2:
    introduceturt(player2, name2.upper(), -360, 210)


############################# The Race #############################


# Runs an infinite loop that continously moves each turtle opponent simultaneously
# If a turtle hits a moving obstacle (coin) or edge, they go back to start
# Computer controlled turtles make random movements but at set distances and can turn at corners
while True:
    for coin in coinlist:
        # For each obstacle
        for player in turtlelist:
            # For each turtle
            if player.distance(coin) < 20:
                # If the turtle touched the coin, the turtle resets back to beginning
                resetturtle(player)
        # Coin bounces back when it hits edge
        if outofbounds(coin):
            coin.seth(coin.heading() + 180)
        coin.forward(3)

    if reachedfinish(player1):
        # If player crosses finish line, while loop breaks, game ends
        player1.ht()
        break
    if outofbounds(player1):
        # If player touches edge
        ### Reset speed and place player back to beginning
        resetturtle(player1)
        playerspeed1 = 1
    else:
        # Otherwise, keep player moving at its speed
        player1.forward(playerspeed1)

    if num_player == 2:
        # If multiplayer, make same comparisons as player 1 but with player 2 turtle
        if reachedfinish(player2):
            player2.ht()
            break
        if outofbounds(player2):
            resetturtle(player2)
            playerspeed2 = 1
        else:
            player2.forward(playerspeed2)

    # Checks if they reach finish line first before players
    if reachedfinish(adam) or reachedfinish(bob):
        break
    # Each turtle opponent moves simultaneously as they each move small distances randomly generated rapidly
    # If they touch the edge
    ### Reset speed and place them back to beginning
    if moveturtle(adam, starting_pos_A, distance1, distance2):
        resetturtle(adam)
    if moveturtle(bob, starting_pos_B, distance1, distance2):
        resetturtle(bob)


############################# End Game #############################


goto(-190, 40)
if reachedfinish(adam) or reachedfinish(bob):
    # If other (computer controlled) turtles reached finish line first
    word_player = "both " if num_player == 2 else ""
    print("Computer wins. You %slose." % word_player)
    write("You %slose." % word_player, align = 'Center', font = ("Arial", 20, "normal"))

elif reachedfinish(player1):
    # If player 1 finishes first
    print("Player 1 wins")
    write("%s wins! You have beaten Mr. Adam and Mr. Bob" % name1, align = 'Center', font = ("Arial", 30, "normal"))

elif num_player == 2 and reachedfinish(player2):
    # If player 2 finishes first
    print("Player 2 wins")
    write("%s wins! You have beaten Mr. Adam and Mr. Bob" % name2, align = 'Center', font = ("Arial", 30, "normal"))

goto(-190, 20)
write("Click anywhere to exit.", align = 'Center', font = ("Arial", 20, "normal"))
exitonclick()
