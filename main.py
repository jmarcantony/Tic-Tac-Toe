from board import Board
from art import logo
import time
import os



def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
        
  
def main():
    board = Board()

    while True:
        board.print_board()

        loc = input(f"Enter co-ordinates to plot {board.turn}: ")
        success = board.plot(loc)

        game_over, winner = board.check_winner()

        if success:
            if not game_over:
                clear()
                board.switch_turn()
            else:
                clear()
                board.print_board()
                print("\n    GAME OVER    \n")
                if winner != "DRAW":
                    print(f"{winner} won!")
                else:
                    print("Its a draw!")
                break
        else:
            time.sleep(1)
            clear()


if __name__ == "__main__":
    print(logo)
    print("\n[*] PRESS ENTER TO START")
    input()
    clear()

    main()
