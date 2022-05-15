import chess_engine
from enums import Player
import random

class chess_ai:
    endgameMaterialStart = 160.0

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
            res = []
            for move_pair in all_possible_moves:
                game_state.move_piece(move_pair[0], move_pair[1], True)
                evaluation = self.minimax_white(game_state, depth - 1, alpha, beta, False, "white")
                game_state.undo_move()

                if max_evaluation < evaluation:
                    max_evaluation = evaluation
                    best_possible_move = move_pair
                    res.clear()
                    res.append(move_pair)
                elif max_evaluation == evaluation:
                    res.append(move_pair)
                alpha = max(alpha, evaluation)
                if beta <= alpha:
                    break
            if depth == 2:
                cur = -9999
                final = []
                for move_pair in res:
                    (x, y) = (move_pair[0][0], move_pair[0][1])
                    (a, b) = (move_pair[1][0], move_pair[1][1])
                    tmp = - abs(self.get_piece_value(game_state.get_piece(x, y), player_color))
                    if game_state.is_valid_piece(a, b):
                        tmp += 10 * abs(self.get_piece_value(game_state.get_piece(a, b), player_color))
                    if tmp > cur:
                        cur = tmp
                        final = move_pair
                return final
            else:
                return max_evaluation
        else:
            min_evaluation = 10000000
            all_possible_moves = game_state.get_all_legal_moves("white")
            res = []
            for move_pair in all_possible_moves:
                game_state.move_piece(move_pair[0], move_pair[1], True)
                evaluation = self.minimax_white(game_state, depth - 1, alpha, beta, True, "black")
                game_state.undo_move()

                if min_evaluation > evaluation:
                    min_evaluation = evaluation
                    best_possible_move = move_pair
                    res.clear()
                    res.append(move_pair)
                elif min_evaluation == evaluation:
                    res.append(move_pair)
                beta = min(beta, evaluation)
                if beta <= alpha:
                    break
            if depth == 2:
                cur = -9999
                final = []
                for move_pair in res:
                    (x, y) = (move_pair[0][0], move_pair[0][1])
                    (a, b) = (move_pair[1][0], move_pair[1][1])
                    tmp = - abs(self.get_piece_value(game_state.get_piece(x, y), player_color))
                    if game_state.is_valid_piece(a, b):
                        tmp += 10 * abs(self.get_piece_value(game_state.get_piece(a, b), player_color))
                    if tmp > cur:
                        cur = tmp
                        final = move_pair
                return final
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
            res = []
            for move_pair in all_possible_moves:
                game_state.move_piece(move_pair[0], move_pair[1], True)
                evaluation = self.minimax_black(game_state, depth - 1, alpha, beta, False, "black")
                game_state.undo_move()

                if max_evaluation < evaluation:
                    max_evaluation = evaluation
                    best_possible_move = move_pair
                    res.clear()
                    res.append(move_pair)
                elif max_evaluation == evaluation:
                    res.append(move_pair)
                alpha = max(alpha, evaluation)
                if beta <= alpha:
                    break
            if depth == 2:
                cur = -9999
                final = []
                for move_pair in res:
                    (x, y) = (move_pair[0][0], move_pair[0][1])
                    (a, b) = (move_pair[1][0], move_pair[1][1])
                    tmp = - abs(self.get_piece_value(game_state.get_piece(x, y), player_color))
                    if game_state.is_valid_piece(a, b):
                        tmp += 10 * abs(self.get_piece_value(game_state.get_piece(a, b), player_color))
                    if tmp > cur:
                        cur = tmp
                        final = move_pair
                return final
            else:
                return max_evaluation
        else:
            min_evaluation = 10000000
            all_possible_moves = game_state.get_all_legal_moves("black")
            res = []
            for move_pair in all_possible_moves:
                game_state.move_piece(move_pair[0], move_pair[1], True)
                evaluation = self.minimax_black(game_state, depth - 1, alpha, beta, True, "white")
                game_state.undo_move()

                if min_evaluation > evaluation:
                    min_evaluation = evaluation
                    best_possible_move = move_pair
                    res.clear()
                    res.append(move_pair)
                elif min_evaluation == evaluation:
                    res.append(move_pair)
                beta = min(beta, evaluation)
                if beta <= alpha:
                    break
            if depth == 2:
                cur = -9999
                final = []
                for move_pair in res:
                    (x, y) = (move_pair[0][0], move_pair[0][1])
                    (a, b) = (move_pair[1][0], move_pair[1][1])
                    tmp = - abs(self.get_piece_value(game_state.get_piece(x, y), player_color))
                    if game_state.is_valid_piece(a, b):
                        tmp += 10 * abs(self.get_piece_value(game_state.get_piece(a, b), player_color))
                    if tmp > cur:
                        cur = tmp
                        final = move_pair
                return final
            else:
                return min_evaluation

    def evaluate_board(self, game_state, player):
        evaluation_score = 0
        evaluation_score_without_pawn = 0
        friendly_king = game_state._white_king_location if player is Player.PLAYER_2 else game_state._black_king_location
        opponent_king = game_state._white_king_location if player is Player.PLAYER_1 else game_state._black_king_location
        for row in range(0, 8):
            for col in range(0, 8):
                if game_state.is_valid_piece(row, col):
                    evaluated_piece = game_state.get_piece(row, col)
                    evaluation_score += self.get_piece_value(evaluated_piece, player)

                    if evaluated_piece.get_name() is not 'p' and evaluated_piece.get_name() is not 'k' and evaluated_piece.get_player() is player:
                        evaluation_score_without_pawn += self.get_piece_value(evaluated_piece, player)

        end_game_weight = self.endgame_phase_weight(-evaluation_score_without_pawn)
        end_game_eval = self.force_king_eval(friendly_king, opponent_king, end_game_weight)
        
        if player is Player.PLAYER_2:
            return evaluation_score + end_game_eval
        else:
            return evaluation_score + end_game_eval

    def endgame_phase_weight(self, materialCountWithoutPawns):
        multiplier = 1 / self.endgameMaterialStart
        return 1 - min(1, materialCountWithoutPawns * multiplier)

    def force_king_eval(self, friendly_king, opponent_king, end_game_weight):
        eval = 0
        opponent_king_distX_center = max(3 - opponent_king[0], opponent_king[0] - 4)
        opponent_king_distY_center = max(3 - opponent_king[1], opponent_king[1] - 4)
        eval += opponent_king_distX_center + opponent_king_distY_center

        distX_king = abs(friendly_king[0] - opponent_king[0])
        distY_king = abs(friendly_king[1] - opponent_king[1])
        eval += 14 - (distX_king + distY_king)

        return int(eval * 10 * end_game_weight)

    def get_piece_value(self, piece, player):
        if player is Player.PLAYER_1:
            if piece.is_player("black"):
                if piece.get_name() is "k":
                    return 1000
                elif piece.get_name() is "q":
                    return 100
                elif piece.get_name() is "r":
                    return 50
                elif piece.get_name() is "b":
                    return 30
                elif piece.get_name() is "n":
                    return 30
                elif piece.get_name() is "p":
                    return 10
            else:
                if piece.get_name() is "k":
                    return -1000
                elif piece.get_name() is "q":
                    return -100
                elif piece.get_name() is "r":
                    return -50
                elif piece.get_name() is "b":
                    return -30
                elif piece.get_name() is "n":
                    return -30
                elif piece.get_name() is "p":
                    return -10
        else:
            if piece.is_player("white"):
                if piece.get_name() is "k":
                    return 1000
                elif piece.get_name() is "q":
                    return 100
                elif piece.get_name() is "r":
                    return 50
                elif piece.get_name() is "b":
                    return 30
                elif piece.get_name() is "n":
                    return 30
                elif piece.get_name() is "p":
                    return 10
            else:
                if piece.get_name() is "k":
                    return -1000
                elif piece.get_name() is "q":
                    return -100
                elif piece.get_name() is "r":
                    return -50
                elif piece.get_name() is "b":
                    return -30
                elif piece.get_name() is "n":
                    return -30
                elif piece.get_name() is "p":
                    return -10