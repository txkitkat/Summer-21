# main.py

from game import *


def main():
    player_opt = '0'

    while 1:
        printmenu()
        board = [[0]*11]*12
        player_opt = input(" Choose option: ")

        if player_opt == '0' or player_opt == '5':
            print(" Goodbye!")
            break

        elif player_opt == '1':
            chess_pvp(board)
            break
        elif player_opt == '2':
            Chess_PVAI(board)
            break
        elif player_opt == '3':
            AIvAI(board)
            break
        else:
            print(" Invalid input")


def printmenu():
    print("============================")
    print(" Welcome To Cool Cats Chess!")
    print("============================")
    print(" 1. Chess P V. P")
    print(" 2. Chess P V. AI")
    print(" 3. AI v. AI")
    print(" 4. Online Chess P V. P")
    print(" 5. Exit")
    print("============================")


main()


