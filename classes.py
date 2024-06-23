""" 
A game has:
    - A state
    - A board
A game can:
    - Print its state
"""
class Game:
    # Initializer
    def __init__(self, board, state=""):
        self.__state = state
        self.__board = board

    # Getters and Setters
    def get_state(self):
        return self.__state
    
    def set_state(self, state):
        self.__state = state

    def get_board(self):
        return self.__board
    
    def set_board(self, board):
        self.__board = board

    # Prints the game's state
    def print_state(self):
        print(self.get_state())


"""
A mine has:
    - A row (1-indexed)
    - A column (1-indexed)
"""
class Mine:
    # Initializer
    def __init__(self, row, column):
        self.__row = row
        self.__column = column

    # Getters and Setters
    def get_row(self):
        return self.__row
    
    def set_row(self, row):
        self.__row = row

    def get_column(self):
        return self.__column
    
    def set_column(self, column):
        self.__column = column


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

    # Creates a grid of empty squares
    def set_grid(self):
        # Create row
        for i in range(self.height):
            row = []
            # Fill row with empty squares
            for j in range(self.width):
                row.append("-")
            # Add row to grid
            self.grid.append(row)
    

    def place_mines(self):
        for i in range(self.height):
        columns = []
            for j in range(self.width):
                column = ""
        return