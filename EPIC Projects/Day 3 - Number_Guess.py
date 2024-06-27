# Program used to introduce students to random in python by creating
# a random number guessing game. Uses serial terminal for intput / output
# EPIC 2022
# Paul Hummel

from microbit import *
import urandom

rand_num = urandom.randrange(1,101)
#print("random number is ",rand_num)

tries = 0
while True:
    print("Guess a number")
    guess = int(input())
    #print("You guessed",guess)
    tries = tries + 1
    if (rand_num == guess):
        print("You guessed correctly!")
        if (tries == 1):
            print("Amazing! You guessed on the first try")
        else:
            print("It took you",tries,"guesses")
        rand_num = urandom.randrange(1,101)
        tries = 0
    elif (rand_num > guess):
        print("You guessed low")
    else:
        print("You guessed high")
    sleep(100)
