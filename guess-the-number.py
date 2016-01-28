# Guess the Number Mini-Project


# modules
import simplegui
import random
import math


# variables setting the state of the game with range and game messages
lower_bound = 0
upper_bound = 100
game_messages = {"new game": "New game. Range is from",
                 "num_guesses": "Number of guesses remaining:",
                 "player guess": "Guess was",
                 "secret number": "Secret number was",
                 "too low": "Higher!\n",
                 "too high": "Lower!\n",
                 "correct": "Correct!\n",
                 "game over": "G A M E O V E R\n"}


def new_game():
    # A game is always in play. The secret number and remaining guesses are dependent on the state of the game, set automatically at [0,100) but can change to [0,1000). Each new game assigns a value to the global variables secret_number and remaining_guesses, and prints out the current range and the number of guesses remaining.
    global secret_number, remaining_guesses

    secret_number = random.randint(0, upper_bound)

    remaining_guesses = int(math.ceil(math.log(upper_bound - lower_bound + 1, 2)))

    print game_messages["new game"], upper_bound
    print game_messages["num_guesses"], remaining_guesses
    print


def range100():
    # button that changes the range to [0,100) and starts a new game
    global upper_bound
    upper_bound = 100
    new_game()


def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global upper_bound
    upper_bound = 1000
    new_game()


def input_guess(guess):
    # Takes player's guess from frame input, converts it to an integer, and compares it against the secret number to print out one of four responses. Correct guess immediatley start a new game. A counter decrements remaining guesses and will immediately start a new game when it reaches 0.
    int_guess = int(guess)
    print game_messages["player guess"], guess

    global remaining_guesses
    if int_guess == secret_number:
        print game_messages["correct"]
        new_game()
    elif remaining_guesses <= 1:
        print game_messages["secret number"], secret_number
        print game_messages["game over"]
        new_game()
    elif int_guess < secret_number:
        remaining_guesses -= 1
        print game_messages["num_guesses"], remaining_guesses
        print game_messages["too low"]
    elif int_guess > secret_number:
        remaining_guesses -= 1
        print game_messages["num_guesses"], remaining_guesses
        print game_messages["too high"]


# create frame
frame = simplegui.create_frame("Guessing Game", 200, 200)


# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 150)
frame.add_button("Range is [0, 1000)", range1000, 150)
frame.add_input("Enter a guess", input_guess, 150)


# call new_game
new_game()


# always remember to check your completed program against the grading rubric
