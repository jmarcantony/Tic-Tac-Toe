class Board:
    def __init__(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.turn = "X"

    def print_board(self):
        print(f"{self.turn}'s Turn")
        print(f"""
      {self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]}
     ---|---|---
      {self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]}
     ---|---|---
      {self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]}
        """)

    def plot(self, loc):
        if len(loc) == 2:
            try:
                row = int(loc[0]) - 1
                col = int(loc[1]) - 1
                cell = self.board[row][col]
                if cell == " ":
                    self.board[row][col] = self.turn
                else:
                    print("\n[-] Cell is already taken! try again.")
                    return False
                return True
            except:
                print("\n[-] Something went wrong!, try again")
                return False
        else:
            print("\n[-] Invalid Co-ordinates!, try again.")
            return False

    def check_x(self):

        # Check Rows
        if self.board[0][0] == "X" and self.board[0][1] == "X" and self.board[0][2] == "X":
            return True
        elif self.board[1][0] == "X" and self.board[1][1] == "X" and self.board[1][2] == "X":
            return True
        elif self.board[2][0] == "X" and self.board[2][1] == "X" and self.board[2][2] == "X":
            return True

        # Check Diagonals
        elif self.board[0][0] == "X" and self.board[1][1] == "X" and self.board[2][2] == "X":
            return True
        elif self.board[0][2] == "X" and self.board[1][1] == "X" and self.board[2][0] == "X":
            return True

        # Check Columns
        elif self.board[0][0] == "X" and self.board[1][0] == "X" and self.board[2][0] == "X":
            return True
        elif self.board[0][1] == "X" and self.board[1][1] == "X" and self.board[2][1] == "X":
            return True
        elif self.board[0][2] == "X" and self.board[1][2] == "X" and self.board[2][2] == "X":
            return True
        else:
            return False

    def check_o(self):

        # Check Rows
        if self.board[0][0] == "O" and self.board[0][1] == "O" and self.board[0][2] == "O":
            return True
        elif self.board[1][0] == "O" and self.board[1][1] == "O" and self.board[1][2] == "O":
            return True
        elif self.board[2][0] == "O" and self.board[2][1] == "O" and self.board[2][2] == "O":
            return True
        
        # Check Diagonals
        elif self.board[0][0] == "O" and self.board[1][1] == "O" and self.board[2][2] == "O":
            return True
        elif self.board[0][2] == "O" and self.board[1][1] == "O" and self.board[2][0] == "O":
            return True

        # Check Columns
        elif self.board[0][0] == "O" and self.board[1][0] == "O" and self.board[2][0] == "O":
            return True
        elif self.board[0][1] == "O" and self.board[1][1] == "O" and self.board[2][1] == "O":
            return True
        elif self.board[0][2] == "O" and self.board[1][2] == "O" and self.board[2][2] == "O":
            return True
        else:
            return False

    def check_draw(self):
        draw = True
        for row in self.board:
            for cell in row:
                if cell == " ":
                    draw = False
        return draw

    def switch_turn(self):
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    def check_winner(self):
        if self.check_x():
            return True, "X"
        elif self.check_o():
            return True, "O"
        elif self.check_draw():
            return True, "DRAW"
        else:
            return False, None
