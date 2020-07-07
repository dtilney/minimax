import ttt

b = ttt.Board(3, 4, 3)
b.make_move(1, 1, 'X')
b.make_move(1, 2, 'X')
b.make_move(1, 3, 'X')
print(b)
print(b.winner())