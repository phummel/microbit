# Two player tic-tac-toe game that uses serial terminal for intput / output
# Improved version with more features
# EPIC 2022
# Paul Hummel

from microbit import *

board = [" "," "," "," "," "," "," "," "," "]

def print_board_key():
    print(" 0 | 1 | 2 ")
    print("-----------")
    print(" 3 | 4 | 5 ")
    print("-----------")
    print(" 6 | 7 | 8 ")

def print_board():
    print("")
    print(" "+board[0]+" | "+board[1]+" | "+board[2]+" ")
    print("-----------")
    print(" "+board[3]+" | "+board[4]+" | "+board[5]+" ")
    print("-----------")
    print(" "+board[6]+" | "+board[7]+" | "+board[8]+" ")

def clear_board():
    for i in range(len(board)):
        board[i] = " "

def check_win():
    #Check horizontal wins
    if (board[0] == board[1] == board[2]) and (board[0] != " "):
        return board[0]
    if (board[3] == board[4] == board[5]) and (board[3] != " "):
        return board[3]
    if (board[6] == board[7] == board[8]) and (board[6] != " "):
        return board[6]
    #check vertical wins
    if (board[0] == board[3] == board[6]) and (board[0] != " "):
        return board[0]
    if (board[1] == board[4] == board[7]) and (board[1] != " "):
        return board[1]
    if (board[2] == board[5] == board[8]) and (board[2] != " "):
        return board[2]
    #check diagonal wins
    if (board[0] == board[4] == board[8]) and (board[0] != " "):
        return board[0]
    if (board[2] == board[4] == board[6]) and (board[2] != " "):
        return board[2]
    # no winner, return " "
    return " "
    
print_board()
player = "X"
# Code in a 'while True:' loop repeats forever
while True:
    move = int(input("Player "+player+" Where would you like to move? "))
    #check for valid move
    while (move not in range(9)):
        print("Invalid Move. Select 0 - 8")
        move = int(input("Player "+player+" Where would you like to move? "))
    
    if (board[move] == " "):
        board[move] = player
        winner = check_win()
        if (winner == " "):  #no winner
            if (player == "X"):
                player = "O"
            else:
                player = "X"
        else:
            print_board()
            print("Player",winner,"Wins!!!")
            input("Press enter to play again")
            clear_board()
            player = "X"
    else:
        print("Space already taken")
    print_board()
    
