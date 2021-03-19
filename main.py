from board import Board
from art import logo
import os
import time


def main():
    board = Board()

    while True:
        board.print_board()

        loc = input(f"Enter co-ordinates to plot {board.turn}: ")
        success = board.plot(loc)

        game_over, winner = board.check_winner()

        if success:
            if not game_over:
                os.system("cls")
                board.switch_turn()
            else:
                os.system("cls")
                board.print_board()
                print("\n    GAME OVER    \n")
                if winner != "DRAW":
                    print(f"{winner} won!")
                else:
                    print("Its a draw!")
                break
        else:
            time.sleep(1)
            os.system("cls")


if __name__ == "__main__":
    print(logo)
    print("\n[*] PRESS ENTER TO START")
    input()
    os.system("cls")

    main()
