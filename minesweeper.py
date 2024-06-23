""" 
A game has:
    - A state
    - A board
A game can:
    - Print its state
"""
class Game:
    def __init__(self, state, board):
        self.state = state
        self.board = board

    def print_state(self):
        print(self.state)

""" 
A board has:
    - A width
    - A height
    - A grid(list of lists) of rows(lists) with:
        - Squares(elements) that are:
            - Empty
            - Mines
    - Mines
 A board can:
   - Place its mines
"""
class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = []
        self.mines = []

    def place_mines(self):
        return



def main():
    width = 4
    height = 4
    board = Board(width, height)

    for i in range(height):
        columns = []
        for j in range(width):
            column = ""

    
    return


if __name__ == "__main__":
    main()