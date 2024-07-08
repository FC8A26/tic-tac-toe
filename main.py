import sys
import os
import platform

board = [0, 0, 0, 0, 0, 0, 0, 0, 0,]


def main():
    while True:        
        reload_screen()

        # Bot move
        ...

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
            

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


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
    print("")    


def reload_screen():
    clear_screen()
    print_board()
    print("")    
    if not 0 in board:
        input("Game over")
        clear_screen()
        sys.exit()
    

main()
