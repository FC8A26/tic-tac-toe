import sys
import os
import platform

board = [0, 0, 0, 0, 0, 0, 0, 0, 0]


def main():
    try:
        tutorial()

        while True:
            # Bot move
            reload_screen()
            bot_move()

            # Player move       
            while True:
                reload_screen()
                index = input("Position: ")
                try:
                    index = int(index)
                except ValueError:
                    input("Please input an integer")
                    continue
                if index < 0 or index > 8:
                    input("Out of range")
                elif board[index] != 0:
                    input("Square is already occupied")
                else:
                    board[index] = 2
                    break
    except KeyboardInterrupt:
        clear_screen()
        sys.exit()
            

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def tutorial():
    clear_screen()
    print("Welcome to Tic-Tac-Toe!")
    print("You play as O's. On your turn, enter a position:\n")
    print("0 | 1 | 2")
    print("---------")
    print("3 | 4 | 5")
    print("---------")
    print("6 | 7 | 8\n")
    input("Click enter to start.")


def print_board():
    for i in range(3):
        for j in range(3):
            if board[3*i + j] == 1:
                print("X", end="")
            elif board[3*i + j] == 2:
                print("O", end="")
            else:
                print(" ", end="")
            if j != 2:
                print(" | ", end="")
        if i != 2:
            print("\n---------")
    print("\n")


def get_gamestate():
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]

    # Check for win/lose
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != 0:
            return board[combo[0]]

    # Check for draw
    if not 0 in board:
        return 0


def reload_screen():
    clear_screen()
    print_board()
    
    # Check for game over
    gamestate = get_gamestate()
    if gamestate == 1:
        sys.exit("Bot wins")
    elif gamestate == 2:
        sys.exit("Player wins")
    elif gamestate == 0:
        sys.exit("Draw")


def bot_move():
    index = 0
    while True:
        if board[index] == 0:
            break
        else:
            index += 1
    board[index] = 1


main()
