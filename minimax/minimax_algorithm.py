import numpy as np

class Player:
    def __init__(self, type):
        self.type = type
        self.children = []
        self.moves = []
        self.best_move
        self.state = State()
        
    def set_children(self, state):
        for i in np.nditer(state.board):
            if i == 0:
                child = Player(self.type * (-1))
                self.children.append(child)

    def set_best_move(self, move):
        self.best_move = move

    def get_moves(self):
        return self.moves

    def add_move(self, move):
        self.moves.append(move)

class State:
    def __init__(self, board=np.zeros((3, 3)), current_move=1):
        self.board = board
        self.current_move = current_move
        self.terminal = 0
        self.children = []
    
    def set_children(self): 
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    child = State(self.board, self.current_move*(-1))
                    child.board[i][j] + child.current_move
                    self.children.append(child)
        

# class Game:
#     def __init__(self):
#         pass

def heuristic(state):
    matrix = np.array([[3, 2, 3], [2, 4, 2], [3, 2, 3]])
    value = matrix * state.board
    return np.sum(value)


def minimax(depth, player, state, game):
    if depth == 0 or state.terminal == 1:
        return heuristic(state)
    #player.set_children()
    state.set_children()
    player.type *= (-1)
    for child in state.children:
        player.add_move(minimax(depth - 1, player, child, game))
    player.type *= (-1)
    if player.type is 1: # 1 = krzyzyk
        player.set_best_move(max(player.get_moves()))
    else:
        player.set_best_move(min(player.get_moves()))
    return player.set_best_move

