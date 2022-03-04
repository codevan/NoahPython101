import os
os.system("clear")

class Board():
    def __init__(self):
        self.cells = ["", "X", "O", "X", "", "", "", "", ""]
    def display(self):
        print(" %s | %s | %s " % (self.cells[1], self.cells[2], self.cells[3]))


board = Board()
board.display()