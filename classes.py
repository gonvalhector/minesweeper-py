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
A mine has:
    - A row (1-indexed)
    - A column (1-indexed)
"""
class Mine:
    def __init__(self, row, column):
        self.row = row
        self.column = column


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
        for i in range(self.height):
        columns = []
            for j in range(self.width):
                column = ""
        return