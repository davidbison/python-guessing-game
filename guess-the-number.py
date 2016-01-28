# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    secret_number = random.randint(1, 99)
    print secret_number
    return secret_number


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game

    # remove this when you add your code
    pass

def range1000():
    # button that changes the range to [0,1000) and starts a new game

    pass

def input_guess(guess):
    # main game logic goes here
    int_guess = int(guess)
    print "Guess was " + guess

    game_messages = ["Higher", "Lower", "Correct"]
    if int_guess < secret_number:
        print game_messages[0]
    elif int_guess > secret_number:
        print game_messages[1]
    elif int_guess == secret_number:
        print game_messages[2]


# create frame
frame = simplegui.create_frame("Guessing Game", 200, 200)
frame.add_input("Enter guess:", input_guess, 100)

# register event handlers for control elements and start frame


# call new_game
new_game()


# always remember to check your completed program against the grading rubric
