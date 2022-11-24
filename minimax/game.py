import numpy as np
from minimax_algorithm import *
from print_board import print_board
    

class Game:
    def __init__(self):
        self.player = Player(1)
        self.state = State()
        self.winner = None
        self.current_move = 1

    def print_comments(self, minmax):
        if minmax >= 1000:
            print("Zwyciężył gracz X")
            self.winner = "X"
            return            
        elif minmax <= -1000:
            print("Zwyciężył gracz O")
            self.winner = "O"
            return 
        else:               
            print("Remis")
            return
    
    def set_for_new_round(self, board):
        self.current_move *= -1
        self.state = State(board, self.current_move)
        self.player = Player(self.current_move)
        

    def game(self, depth1, depth2):
        while(self.state.terminal == 0):
            if self.player.type == 1:
                minmax = minimax(depth1, self.player, self.state)
            else:
                minmax = minimax(depth2, self.player, self.state)
            if self.state.terminal == 1:
                self.print_comments(minmax)
                return
            board = copy.deepcopy(self.state.children[self.player.moves.index(minmax)].board)
            print_board(board)
            self.set_for_new_round(board)

            
            


game = Game()
game.game(4, 4)

