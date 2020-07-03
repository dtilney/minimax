'''
ttt.py
Module for m x n tic tac toe
'''

class Board:
    def __init__(self, R, C, N):
        self.R = R
        self.C = C
        self.N = N
        self.state = [ [ str(c + self.C * r) for c in range(self.C) ] for r in range(self.R) ]

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
 
