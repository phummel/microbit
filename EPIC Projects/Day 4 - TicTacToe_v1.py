# Two player tic-tac-toe game that uses serial terminal for intput / output
# EPIC 2022
# Paul Hummel

from microbit import *

board = [" ", " ", " ", 
         " ", " ", " ",
         " ", " ", " "]

def print_board():
    print(" ",board[0],"|",board[1],"|",board[2])
    print(" -----------")
    print(" ",board[3],"|",board[4],"|",board[5])
    print(" -----------")
    print(" ",board[6],"|",board[7],"|",board[8])

def check_win(player):
    # checking rows
    if (player == board[0] == board[1] == board[2]):
        return True
    if (player == board[3] == board[4] == board[5]):
        return True
    if (player == board[6] == board[7] == board[8]):
        return True
    # checking columns
    if (player == board[0] == board[3] == board[6]):
        return True
    if (player == board[1] == board[4] == board[7]):
        return True
    if (player == board[2] == board[5] == board[8]):
        return True
    # check diagonals
    if (player == board[0] == board[4] == board[8]):
        return True
    if (player == board[2] == board[4] == board[6]):
        return True
    return False

turn = "X"
turns = 0
# Code in a 'while True:' loop repeats forever
while True:
    print_board()
    print("Player",turn,"select a spot")
    spot = int(input())
    if (board[spot] == " "):
        board[spot] = turn
        turns = turns + 1
        if (check_win(turn)):
            print("Player",turn,"Won!!!!")
            board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
            turns = 0
            print("Press enter to play again")
            input()
        else:
            if (turns == 9):
                print("The game was a tie!")
                board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
                turns = 0
                print("Press enter to play again")
                input()
            if (turn == "X"):
                turn = "O"
            else:
                turn = "X"
    else:
        print("That space is already used. Pick again")






