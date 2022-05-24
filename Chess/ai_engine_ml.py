import chess_engine
from enums import Player
import random
from tensorflow.keras import models
import numpy


class chess_ai:
    model = models.load_model('train/model.h5')

    def minimax_white(self, game_state, depth, alpha, beta, maximizing_player, player_color):
        csc = game_state.checkmate_stalemate_checker()
        if maximizing_player:
            if csc == 0:
                return 5000000
            elif csc == 1:
                return -5000000
            elif csc == 2:
                return 100
        elif not maximizing_player:
            if csc == 1:
                return -5000000
            elif csc == 0:
                return 5000000
            elif csc == 2:
                return 100

        if depth <= 0 or csc != 3:
            return self.evaluate_board(game_state, Player.PLAYER_1)

        if maximizing_player:
            max_evaluation = -10000000
            all_possible_moves = game_state.get_all_legal_moves("black")
            for move_pair in all_possible_moves:
                game_state.move_piece(move_pair[0], move_pair[1], True)
                evaluation = self.minimax_white(
                    game_state, depth - 1, alpha, beta, False, "white")
                game_state.undo_move()
                if max_evaluation < evaluation:
                    max_evaluation = evaluation
                    best_possible_move = move_pair

                alpha = max(alpha, evaluation)
                if beta <= alpha:
                    break
            if depth == 1:
                return best_possible_move
            else:
                return max_evaluation
        else:
            min_evaluation = 10000000
            all_possible_moves = game_state.get_all_legal_moves("white")
            for move_pair in all_possible_moves:
                game_state.move_piece(move_pair[0], move_pair[1], True)
                evaluation = self.minimax_white(
                    game_state, depth - 1, alpha, beta, True, "black")
                game_state.undo_move()

                if min_evaluation > evaluation:
                    min_evaluation = evaluation
                    best_possible_move = move_pair

                beta = min(beta, evaluation)
                if beta <= alpha:
                    break
            if depth == 1:
                return best_possible_move
            else:
                return min_evaluation

    def minimax_black(self, game_state, depth, alpha, beta, maximizing_player, player_color):
        csc = game_state.checkmate_stalemate_checker()
        if maximizing_player:
            if csc == 1:
                return 5000000
            elif csc == 0:
                return -5000000
            elif csc == 2:
                return 100
        elif not maximizing_player:
            if csc == 0:
                return -5000000
            elif csc == 1:
                return 5000000
            elif csc == 2:
                return 100

        if depth <= 0 or csc != 3:
            return self.evaluate_board(game_state, Player.PLAYER_2)

        if maximizing_player:
            max_evaluation = -10000000
            all_possible_moves = game_state.get_all_legal_moves("white")
            for move_pair in all_possible_moves:
                game_state.move_piece(move_pair[0], move_pair[1], True)
                evaluation = self.minimax_black(
                    game_state, depth - 1, alpha, beta, False, "black")
                game_state.undo_move()

                if max_evaluation < evaluation:
                    max_evaluation = evaluation
                    best_possible_move = move_pair

                alpha = max(alpha, evaluation)
                if beta <= alpha:
                    break
            if depth == 1:
                return best_possible_move
            else:
                return max_evaluation
        else:
            min_evaluation = 10000000
            all_possible_moves = game_state.get_all_legal_moves("black")
            for move_pair in all_possible_moves:
                game_state.move_piece(move_pair[0], move_pair[1], True)
                evaluation = self.minimax_black(
                    game_state, depth - 1, alpha, beta, True, "white")
                game_state.undo_move()

                if min_evaluation > evaluation:
                    min_evaluation = evaluation
                    best_possible_move = move_pair

                beta = min(beta, evaluation)
                if beta <= alpha:
                    break
            if depth == 1:
                return best_possible_move
            else:
                return min_evaluation

    def get_index(self, piece):
        res = 0
        if piece.get_name() == 'p':
            res = 0
        elif piece.get_name() == 'r':
            res = 1
        elif piece.get_name() == 'b':
            res = 2
        elif piece.get_name() == 'n':
            res = 3
        elif piece.get_name() == 'q':
            res = 4
        elif piece.get_name() == 'k':
            res = 5

        if piece.get_player() == Player.PLAYER_2:
            res += 6
        return res

    def split_dims(self, game_state):
        board3d = numpy.zeros((14, 8, 8), dtype=numpy.int8)

        for row in range(0, 8):
            for col in range(0, 8):
                if game_state.is_valid_piece(row, col):
                    piece = game_state.get_piece(row, col)
                    board3d[self.get_index(piece)][row][col] = 1

        white_moves = game_state.get_all_legal_moves("white")
        black_moves = game_state.get_all_legal_moves("black")
        for move_pair in white_moves:
            board3d[12][move_pair[1][0]][move_pair[1][1]] = 1
        for move_pair in black_moves:
            board3d[13][move_pair[1][0]][move_pair[1][1]] = 1

        return board3d

    def evaluate_board(self, game_state, player):
        board3d = self.split_dims(game_state)
        board3d = numpy.expand_dims(board3d, 0)
        res = self.model(board3d)[0][0]
        if player == Player.PLAYER_1:
            res *= -1
        return res
