import chess_engine
from enums import Player
import random

class chess_random:
    def get_move(self, game_state, player):
        all_possible_moves = game_state.get_all_legal_moves(player)
        return random.choice(all_possible_moves)