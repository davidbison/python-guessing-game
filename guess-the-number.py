# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math


# state of first run set to (1,100]
lower_bound = 0
upper_bound = 99
game_messages = ["Higher!\n", "Lower!\n", "Correct!\n", "Guess was ", "Number of remaining guesses is"]


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, remaining_guesses

    secret_number = random.randint(0, upper_bound)

    remaining_guesses = int(math.ceil(math.log(upper_bound - lower_bound + 1, 2)))

    print "New game. Range is from 0 to", upper_bound + 1
    print "Number of remaining guesses is", remaining_guesses
    print secret_number
    print


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    global upper_bound
    upper_bound = 99
    new_game()


def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global upper_bound
    upper_bound = 999
    new_game()


def input_guess(guess):
    # main game logic goes here
    int_guess = int(guess)
    print game_messages[3] + guess

    global remaining_guesses
    if int_guess < secret_number:
        remaining_guesses -= 1
        print game_messages[4], remaining_guesses
        print game_messages[0]
    elif int_guess > secret_number:
        remaining_guesses -= 1
        print game_messages[4], remaining_guesses
        print game_messages[1]
    elif int_guess == secret_number:
        print game_messages[2]
        new_game()


# create frame
frame = simplegui.create_frame("Guessing Game", 200, 200)


# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 150)
frame.add_button("Range is [0, 1000)", range1000, 150)
frame.add_input("Enter a guess", input_guess, 150)


# call new_game
new_game()


# always remember to check your completed program against the grading rubric
