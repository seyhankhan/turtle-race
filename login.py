########### Seyhan Van Khan
########### Turtle Race
########### Race turtles in a multiple difficulty racecourse while avoiding obstacles
########### September 2018
""" Functions:
        menu() - Introduces the game, user chooses game settings (single or multiplayer), sets difficulty, can look at control setting
        attribute(playerturtle) - Allows player to design its turtle whether random or customised
"""

from random import randint, choice
import turtle


# Lists contain all valid colours & shapes that is available for user to choose
colours = ["blue", "brown", "gold", "green", "grey", "orange", "pink", "purple", "red", "turquoise", "yellow"]
shapes = ["arrow", "turtle", "triangle"]

def menu():
    # User chooses whether he wants singleplayer or multiplayer
    # User can look at control settings
    gametype = input("""
Welcome to Turtle Race.

Here you race against 2 opponents (Mr Adam and Mr Bob)

Would you like to go singleplayer or multiplayer? """)

    # User can choose whether he wants to include Player 2
    while "single" not in gametype.lower() and "multi" not in gametype.lower():
        gametype = input("Singleplayer or multiplayer? ")
    no_players = 1 if "single" in gametype.lower() else 2

    choice_display_controls = input("Would you like to see the controls? ")
    if "y" in choice_display_controls.lower():
        # If user types a word with the letter y
        ### Control settings are shown
        print("""

Player 1:
    UP arrow - accelerate
    DOWN arrow - brake
    LEFT arrow - turn left
    RIGHT arrow - turn right
""")
        if no_players == 2:
            print("""
Player 2:
    W - accelerate
    S - brake
    A - turn left
    D - turn right

""")

    level = ""
    while "easy" not in level.lower() and "medium" not in level.lower() and "hard" not in level.lower():
        level = input("Easy, medium or hard? ")
    if "easy" in level.lower():
        framedelay = 3
        no_coins = 2
    elif "medium" in level.lower():
        framedelay = randint(4, 5)
        no_coins = 3
    else:
        framedelay = 8
        no_coins = 3

    return no_players, framedelay, no_coins



def attribute(player):
    # User can customise their turtle's shape and colour
    # If indecisive, user can just randomise it
    name = input("Player Name: ")
    while name == "" or len(name) > 8:
        name = input("Must be 1 - 8 characters long\nPlayer Name: ")

    usr_choice = ""
    while "custom" not in usr_choice.lower() and "random" not in usr_choice.lower():
        # User must type a word that either has the phrase custom or random in it (allows for many combinations)
        usr_choice = input("Would you like to customise your Turtle or randomise it? ")

    if "custom" in usr_choice.lower():
        # If the phrase "custom" is in choice
        ### User can choose the colour & shape
        colour = input("Colour of turtle: ").lower()
        while colour.lower() not in colours:
            colour = input("\nColour not available. Please input another\nColour of turtle: ").lower()

        shape = ""
        print(' - '.join(shapes))
        while shape.lower() not in shapes:
            shape = input("Shape of player: ").lower()

    else:
        # If the phrase "random" is in choice
        # User is indecisive, so computer randomly picks the attribute from the list COLOURS and SHAPES
        colour = choice(colours)
        shape = choice(shapes)

    # Gives the turtle the colour attribute and shape attribute
    player.color(colour)
    player.shape(shape)
    return name
