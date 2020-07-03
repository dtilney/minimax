'''
Implements the minimax algorithm
'''

'''
minimax algorithm

to choose the best move, find the scores of each move, and then choose the highest scoring move.
'''

def best_move(state, maximizing_player):
    if maximizing_player:
        '''
        argmax a in actions of min_value(result(a, state)
        '''
        best_move_value = -1 * float(inf)
        best_move = None
        for a in state.actions():
            v = min_value(
            if v > best_move_value:
            
    
