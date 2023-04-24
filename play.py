from itertools import cycle
from random import choice

from tic_tac_toe import tic_tac_toe_winner

board = ' '*9
symbol = cycle('XO')

while ' ' in board:
    field = choice([n for n, s in enumerate(board) if s == ' '])
    board = board[:field] + next(symbol) + board[field+1:]
    print(board)
    winner = tic_tac_toe_winner(board)
    if winner is not None:
        print(f'{winner} won!')
        break
else:
    print('Tie!')