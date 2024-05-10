"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    symbols = [symbol for row in board for symbol in row]
    if symbols.count('O') < symbols.count('X'):
        return 'O'
    else:
        return 'X'


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return set([(i, j) for i in range(3) for j in range(3) if not board[i][j]])


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]]:
        raise NameError('Incorrect action!')
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check rows 
    for row in board:
        if row[0] and row[0] == row[1] == row[2]:
            return row[0]
    # check cols 
    for col in range(3):
        if board[0][col] and board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]
    # check diagonally 
    if board[0][0] and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[2][0] and board[2][0] == board[1][1] == board[0][2]:
        return board[2][0]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) or sum(board, []).count(None) == 0:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    return 1 if win == 'X' else -1 if win == 'O' else 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    move = ()
    if player(board) == 'X':
        best = -2
        for action in actions(board):
            nv = minv(result(board, action))
            if nv > best:
                best = nv
                move = action
    else:
        best = 2
        for action in actions(board):
            nv = maxv(result(board, action))
            if nv < best:
                best = nv
                move = action
    return move


def minv(board, v2=-2):
    if terminal(board):
        return utility(board)
    v = 2
    for action in actions(board):
        v = min(v, maxv(result(board, action), v))
        if v < v2:
            return v
    return v


def maxv(board, v2=2):
    if terminal(board):
        return utility(board)
    v = -2
    for action in actions(board):
        v = max(v, minv(result(board, action), v))
        if v > v2:
            return v
    return v
