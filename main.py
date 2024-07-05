import os
import platform

board = [1, 0, 0, 0, 0, 0, 0, 0, 0,]


def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


while True:
    clear_screen()
    # Testing
    if board[0] == 1:
        print("X")
    elif board[0] == 2:
        print("O")
    if board[0] == 1:
        board[0] = 2
    elif board[0] == 2:
        board[0] = 1

    # For future
    index = input("Position: ")
    
