import numpy as np
from minimax_algorithm import *
from print_board import print_board
import copy

class Player:
    def __init__(self, type):
        self.type = type
        self.moves = []
        self.best_move = None
        self.children = []

    def add_child(self):
        child = Player(self.type * (-1))
        self.children.append(child)
        return child

    def set_best_move(self, move):
        self.best_move = move

    def add_move(self, move):
        self.moves.append(move)

class State:
    def __init__(self, board=np.zeros((3, 3),int), current_move=1):
        self.board = board
        self.current_move = current_move
        self.terminal = 0
        self.children = []
    
    def set_children_first_time(self):
        for i in range(3):
            child = State(np.zeros((3, 3),int), self.current_move*(-1))
            self.children.append(child)
        self.children[0].board[0][0] -= child.current_move
        self.children[1].board[0][1] -= child.current_move
        self.children[2].board[1][1] -= child.current_move

    def set_children(self):
        if np.array_equal(self.board, np.zeros((3, 3))):
            self.set_children_first_time()
            return
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    child = State(copy.deepcopy(self.board), self.current_move*(-1)) 
                    child.board[i][j] -= child.current_move
                    self.children.append(child)
 
    def set_win(self, i, j):
        if self.board[i][j] == 1:
            return 1
        else:
            return -1


    def check_if_terminal(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] != 0:
                self.terminal = 1
                return self.set_win(i, 0)
            elif self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] != 0:
                self.terminal = 1
                return self.set_win(0, i)
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != 0:
            self.terminal = 1
            return self.set_win(0, 0)
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[2][0] != 0:
            self.terminal = 1
            return self.set_win(2, 0)
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return 0
        self.terminal = 1
        return 0

def heuristic(state):
    matrix = np.array([[3, 2, 3], [2, 4, 2], [3, 2, 3]])
    value = matrix * state.board
    return int(np.sum(value))


def minimax(depth, player, state):
    win = state.check_if_terminal()
    if state.terminal == 1:
        if win == player.type:
            return player.type * depth * 1000
        elif win == 0:
            return heuristic(state)
        else:
            return player.type * (-1) * depth * 1000

    elif depth == 0:
        return heuristic(state)

    state.set_children()
    for child in state.children:
        player_child = player.add_child()
        player.add_move(minimax(depth - 1, player_child, child))

    if player.type == 1:                        #  1 = krzyzyk
        player.set_best_move(max(player.moves))
    else:                                       # -1 = kółko
        player.set_best_move(min(player.moves))

    return player.best_move

