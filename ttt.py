'''
ttt.py
Implements a general tic tac toe board.
'''

class Board:
    '''
    __init__
    Sets up an empty tic tac toe board
    R: number of rows
    C: number of columns
    N: number to get in a row to win
    '''
    def __init__(self, R, C, N):
        self.R = R
        self.C = C
        self.N = N
        self.state = [ [ str(c + self.C * r) for c in range(self.C) ] for r in range(self.R) ]

    '''
    __str__
    Returns the string representation of the current board state
    ex: if self.state = [[1, 2, X], [4, 5, O]] 
        then __str__(self) is:
        +---+---+---+
        | 1 | 2 | X |
        +---+---+---+
        | 4 | 5 | O |
        +---+---+---+
    '''
    def __str__(self):
        max_display_number = self.R * self.C - 1
        entry_width = len(str(max_display_number))
        row_seperator = (('+' + '-' * (entry_width + 2)) * self.C) + '+\n'
        s = ''
        for row in self.state:
            s += row_seperator
            for entry in row:
                s += '| ' + entry.center(entry_width) + ' '
            s += '|\n'
        s += row_seperator
        return s

    def make_move(self, r, c, char):
        self.state[r][c] = char

    '''
    horizontal_winner 
    checks for horizontal wins
    if there is a horizontal win, then returns the winning symbol
    otherwise returns None
    '''
    def horizontal_winner(self):
        for r in range(self.R):
            c = 0; count = 0; current_symbol = None
            while self.C - c + count >= self.N: #A win is possible in this row
                if self.state[r][c] == current_symbol:
                    count += 1
                    if count == self.N:
                        return current_symbol
                else:
                    current_symbol = self.state[r][c]
                    count = 1
                c += 1
        return None

    '''
    vertical_winner 
    checks for vertical wins
    if there is a vertical win, then returns the winning symbol
    otherwise returns None
    '''
    def vertical_winner(self):
        for c in range(self.C):
            r = 0; count = 0; current_symbol = None
            while self.R - r + count >= self.N: #A win is possible in this row
                if self.state[r][c] == current_symbol:
                    count += 1
                    if count == self.N:
                        return current_symbol
                else:
                    current_symbol = self.state[r][c]
                    count = 1
                r += 1
        return None

    def diagonal_winner(self):
        return None
    

    '''
    winner
    returns the winning symbol if the game is over, otherwise returns None
    '''
    def winner(self):
        w = self.horizontal_winner()
        if w is not None:
            return w
        w = self.vertical_winner()
        if w is not None:
            return w
        w = self.diagonal_winner()
        return w


