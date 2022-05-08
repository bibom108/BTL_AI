
from chess_pieces import Rook, Knight, Bishop, Queen, King, Pawn
from enums import Player
# (row, col)
#        0      1      2      3      4      5      6      7 
# 0   [(0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (0,6), (0,7)]
# 1   [(1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,7)]
# 2   [(2,0), (2,1), (2,2), (2,3), (2,4), (2,5), (2,6), (2,7)]
# 3   [(3,0), (3,1), (3,2), (3,3), (3,4), (3,5), (3,6), (3,7)]
# 4   [(4,0), (4,1), (4,2), (4,3), (4,4), (4,5), (4,6), (4,7)]
# 5   [(5,0), (5,1), (5,2), (5,3), (5,4), (5,5), (5,6), (5,7)]
# 6   [(6,0), (6,1), (6,2), (6,3), (6,4), (6,5), (6,6), (6,7)]
# 7   [(7,0), (7,1), (7,2), (7,3), (7,4), (7,5), (7,6), (7,7)]
# '''

class game_state:
    # Initialize 2D array to represent the chess board
    def __init__(self):
        # The board is a 2D array
        # TODO: Change to a numpy format later
        # self.white_captives = []
        # self.black_captives = []
        self.move_log = []
        self.white_turn = False
        self.can_en_passant_bool = False
        self._en_passant_previous = (-1, -1)
        self.checkmate = False
        self.stalemate = False

        self._is_check = False
        self._white_king_location = [0, 3]
        self._black_king_location = [7, 3]

        self.white_king_can_castle = [True, True,
                                      True]  # Has king not moved, has Rook1(col=0) not moved, has Rook2(col=7) not moved
        self.black_king_can_castle = [True, True, True]

        # Initialize White pieces
        white_rook_1 = Rook('r', 0, 0, Player.PLAYER_1)
        white_rook_2 = Rook('r', 0, 7, Player.PLAYER_1)
        white_knight_1 = Knight('n', 0, 1, Player.PLAYER_1)
        white_knight_2 = Knight('n', 0, 6, Player.PLAYER_1)
        white_bishop_1 = Bishop('b', 0, 2, Player.PLAYER_1)
        white_bishop_2 = Bishop('b', 0, 5, Player.PLAYER_1)
        white_queen = Queen('q', 0, 4, Player.PLAYER_1)
        white_king = King('k', 0, 3, Player.PLAYER_1)
        white_pawn_1 = Pawn('p', 1, 0, Player.PLAYER_1)
        white_pawn_2 = Pawn('p', 1, 1, Player.PLAYER_1)
        white_pawn_3 = Pawn('p', 1, 2, Player.PLAYER_1)
        white_pawn_4 = Pawn('p', 1, 3, Player.PLAYER_1)
        white_pawn_5 = Pawn('p', 1, 4, Player.PLAYER_1)
        white_pawn_6 = Pawn('p', 1, 5, Player.PLAYER_1)
        white_pawn_7 = Pawn('p', 1, 6, Player.PLAYER_1)
        white_pawn_8 = Pawn('p', 1, 7, Player.PLAYER_1)
        self.white_pieces = [white_rook_1, white_rook_2, white_knight_1, white_knight_2, white_bishop_1, white_bishop_2,
                             white_queen, white_king, white_pawn_1, white_pawn_2, white_pawn_3, white_pawn_4,
                             white_pawn_5, white_pawn_6, white_pawn_7, white_pawn_8]

        # Initialize Black Pieces
        black_rook_1 = Rook('r', 7, 0, Player.PLAYER_2)
        black_rook_2 = Rook('r', 7, 7, Player.PLAYER_2)
        black_knight_1 = Knight('n', 7, 1, Player.PLAYER_2)
        black_knight_2 = Knight('n', 7, 6, Player.PLAYER_2)
        black_bishop_1 = Bishop('b', 7, 2, Player.PLAYER_2)
        black_bishop_2 = Bishop('b', 7, 5, Player.PLAYER_2)
        black_queen = Queen('q', 7, 4, Player.PLAYER_2)
        black_king = King('k', 7, 3, Player.PLAYER_2)
        black_pawn_1 = Pawn('p', 6, 0, Player.PLAYER_2)
        black_pawn_2 = Pawn('p', 6, 1, Player.PLAYER_2)
        black_pawn_3 = Pawn('p', 6, 2, Player.PLAYER_2)
        black_pawn_4 = Pawn('p', 6, 3, Player.PLAYER_2)
        black_pawn_5 = Pawn('p', 6, 4, Player.PLAYER_2)
        black_pawn_6 = Pawn('p', 6, 5, Player.PLAYER_2)
        black_pawn_7 = Pawn('p', 6, 6, Player.PLAYER_2)
        black_pawn_8 = Pawn('p', 6, 7, Player.PLAYER_2)
        self.black_pieces = [black_rook_1, black_rook_2, black_knight_1, black_knight_2, black_bishop_1, black_bishop_2,
                             black_queen, black_king, black_pawn_1, black_pawn_2, black_pawn_3, black_pawn_4,
                             black_pawn_5,
                             black_pawn_6, black_pawn_7, black_pawn_8]

        self.board = [
            [white_rook_1, white_knight_1, white_bishop_1, white_king, white_queen, white_bishop_2, white_knight_2,
             white_rook_2],
            [white_pawn_1, white_pawn_2, white_pawn_3, white_pawn_4, white_pawn_5, white_pawn_6, white_pawn_7,
             white_pawn_8],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
             Player.EMPTY],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
             Player.EMPTY],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
             Player.EMPTY],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
             Player.EMPTY],
            [black_pawn_1, black_pawn_2, black_pawn_3, black_pawn_4, black_pawn_5, black_pawn_6, black_pawn_7,
             black_pawn_8],
            [black_rook_1, black_knight_1, black_bishop_1, black_king, black_queen, black_bishop_2, black_knight_2,
             black_rook_2]
        ]

    def get_piece(self, row, col):
        if (0 <= row < 8) and (0 <= col < 8):
            return self.board[row][col]

    def is_valid_piece(self, row, col):
        evaluated_piece = self.get_piece(row, col)
        return (evaluated_piece is not None) and (evaluated_piece != Player.EMPTY)

    def get_valid_moves(self, starting_square):
        '''
        remove pins from valid moves (unless the pinned piece move can get rid of a check and checks is empty
        remove move from valid moves if the move falls within a check piece's valid move
        if the moving piece is a king, the ending square cannot be in a check
        '''

        current_row = starting_square[0]
        current_col = starting_square[1]

        if self.is_valid_piece(current_row, current_col):
            valid_moves = []
            moving_piece = self.get_piece(current_row, current_col)
            if self.get_piece(current_row, current_col).is_player(Player.PLAYER_1):
                king_location = self._white_king_location
            else:
                king_location = self._black_king_location
            group = self.check_for_check(king_location, moving_piece.get_player())
            checking_pieces = group[0]
            pinned_pieces = group[1]
            pinned_checks = group[2]
            initial_valid_piece_moves = moving_piece.get_valid_piece_moves(self)

            # immediate check
            if checking_pieces:
                for move in initial_valid_piece_moves:
                    can_move = True
                    for piece in checking_pieces:
                        if moving_piece.get_name() is "k":
                            temp = self.board[current_row][current_col]
                            self.board[current_row][current_col] = Player.EMPTY
                            temp2 = self.board[move[0]][move[1]]
                            self.board[move[0]][move[1]] = temp
                            if not self.check_for_check(move, moving_piece.get_player())[0]:
                                pass
                            else:
                                can_move = False
                            self.board[current_row][current_col] = temp
                            self.board[move[0]][move[1]] = temp2
                        elif move == piece and len(checking_pieces) == 1 and moving_piece.get_name() is not "k" and \
                                (current_row, current_col) not in pinned_pieces:
                            pass
                        elif move != piece and len(checking_pieces) == 1 and moving_piece.get_name() is not "k" and \
                                (current_row, current_col) not in pinned_pieces:
                            temp = self.board[move[0]][move[1]]
                            self.board[move[0]][move[1]] = moving_piece
                            self.board[current_row][current_col] = Player.EMPTY
                            if self.check_for_check(king_location, moving_piece.get_player())[0]:
                                can_move = False
                            self.board[current_row][current_col] = moving_piece
                            self.board[move[0]][move[1]] = temp
                        else:
                            can_move = False
                    if can_move:
                        valid_moves.append(move)
                self._is_check = True
            # pinned checks
            elif pinned_pieces and moving_piece.get_name() is not "k":
                if starting_square not in pinned_pieces:
                    for move in initial_valid_piece_moves:
                        valid_moves.append(move)
                elif starting_square in pinned_pieces:
                    for move in initial_valid_piece_moves:

                        temp = self.board[move[0]][move[1]]
                        self.board[move[0]][move[1]] = moving_piece
                        self.board[current_row][current_col] = Player.EMPTY
                        if not self.check_for_check(king_location, moving_piece.get_player())[0]:
                            valid_moves.append(move)
                        self.board[current_row][current_col] = moving_piece
                        self.board[move[0]][move[1]] = temp
            else:
                if moving_piece.get_name() is "k":
                    for move in initial_valid_piece_moves:
                        temp = self.board[current_row][current_col]
                        temp2 = self.board[move[0]][move[1]]
                        self.board[current_row][current_col] = Player.EMPTY
                        self.board[move[0]][move[1]] = temp
                        if not self.check_for_check(move, moving_piece.get_player())[0]:
                            valid_moves.append(move)
                        self.board[current_row][current_col] = temp
                        self.board[move[0]][move[1]] = temp2
                else:
                    for move in initial_valid_piece_moves:
                        valid_moves.append(move)
            # if not valid_moves:
            #     if self._is_check:
            #         self.checkmate = True
            #     else:
            #         self.stalemate = True
            # else:
            #     self.checkmate = False
            #     self.stalemate = False
            return valid_moves
        else:
            return None

    # 0 if white lost, 1 if black lost, 2 if stalemate, 3 if not game over
    def checkmate_stalemate_checker(self):
        all_white_moves = self.get_all_legal_moves(Player.PLAYER_1)
        all_black_moves = self.get_all_legal_moves(Player.PLAYER_2)
        if self._is_check and self.whose_turn() and not all_white_moves:
            print("white lost")
            return 0
        elif self._is_check and not self.whose_turn() and not all_black_moves:
            print("black lost")
            return 1
        elif not all_white_moves and not all_black_moves:
            return 2
        else:
            return 3

    def get_all_legal_moves(self, player):
        # _all_valid_moves = [[], []]
        # for row in range(0, 8):
        #     for col in range(0, 8):
        #         if self.is_valid_piece(row, col) and self.get_piece(row, col).is_player(player):
        #             valid_moves = self.get_valid_moves((row, col))
        #             if valid_moves:
        #                 _all_valid_moves[0].append((row, col))
        #                 _all_valid_moves[1].append(valid_moves)
        _all_valid_moves = []
        for row in range(0, 8):
            for col in range(0, 8):
                if self.is_valid_piece(row, col) and self.get_piece(row, col).is_player(player):
                    valid_moves = self.get_valid_moves((row, col))
                    for move in valid_moves:
                        _all_valid_moves.append(((row, col), move))
        return _all_valid_moves

    def king_can_castle_left(self, player):
        if player is Player.PLAYER_1:
            return self.white_king_can_castle[0] and self.white_king_can_castle[1] and \
                   self.get_piece(0, 1) is Player.EMPTY and self.get_piece(0, 2) is Player.EMPTY and not self._is_check
        else:
            return self.black_king_can_castle[0] and self.black_king_can_castle[1] and \
                   self.get_piece(7, 1) is Player.EMPTY and self.get_piece(7, 2) is Player.EMPTY and not self._is_check

    def king_can_castle_right(self, player):
        if player is Player.PLAYER_1:
            return self.white_king_can_castle[0] and self.white_king_can_castle[2] and \
                   self.get_piece(0, 6) is Player.EMPTY and self.get_piece(0, 5) is Player.EMPTY and not self._is_check
        else:
            return self.black_king_can_castle[0] and self.black_king_can_castle[2] and \
                   self.get_piece(7, 6) is Player.EMPTY and self.get_piece(7, 5) is Player.EMPTY and not self._is_check

    def promote_pawn(self, starting_square, moved_piece, ending_square):
        while True:
            new_piece_name = input("Change pawn to (r, n, b, q):\n")
            piece_classes = {"r": Rook, "n": Knight, "b": Bishop, "q": Queen}
            if new_piece_name in piece_classes:
                move = chess_move(starting_square, ending_square, self, self._is_check)

                new_piece = piece_classes[new_piece_name](new_piece_name, ending_square[0],
                                                          ending_square[1], moved_piece.get_player())
                self.board[ending_square[0]][ending_square[1]] = new_piece
                self.board[moved_piece.get_row_number()][moved_piece.get_col_number()] = Player.EMPTY
                moved_piece.change_row_number(ending_square[0])
                moved_piece.change_col_number(ending_square[1])
                move.pawn_promotion_move(new_piece)
                self.move_log.append(move)
                break
            else:
                print("Please choose from these four: r, n, b, q.\n")

    def promote_pawn_ai(self, starting_square, moved_piece, ending_square):
        move = chess_move(starting_square, ending_square, self, self._is_check)
        # The ai can only promote the pawn to queen
        new_piece = Queen("q", ending_square[0], ending_square[1], moved_piece.get_player())
        self.board[ending_square[0]][ending_square[1]] = new_piece
        self.board[moved_piece.get_row_number()][moved_piece.get_col_number()] = Player.EMPTY
        moved_piece.change_row_number(ending_square[0])
        moved_piece.change_col_number(ending_square[1])
        move.pawn_promotion_move(new_piece)
        self.move_log.append(move)

    # have to fix en passant for ai
    def can_en_passant(self, current_square_row, current_square_col):
        return False
        # if is_ai:
        #     return False
        # else:
        #     return self.can_en_passant_bool and current_square_row == self.previous_piece_en_passant()[0] \
        #            and abs(current_square_col - self.previous_piece_en_passant()[1]) == 1

    def previous_piece_en_passant(self):
        return self._en_passant_previous

    # Move a piece
    def move_piece(self, starting_square, ending_square, is_ai):
        current_square_row = starting_square[0]  # The integer row value of the starting square
        current_square_col = starting_square[1]  # The integer col value of the starting square
        next_square_row = ending_square[0]  # The integer row value of the ending square
        next_square_col = ending_square[1]  # The integer col value of the ending square

        if self.is_valid_piece(current_square_row, current_square_col) and \
                (((self.whose_turn() and self.get_piece(current_square_row, current_square_col).is_player(
                    Player.PLAYER_1)) or
                  (not self.whose_turn() and self.get_piece(current_square_row, current_square_col).is_player(
                      Player.PLAYER_2)))):

            # The chess piece at the starting square
            moving_piece = self.get_piece(current_square_row, current_square_col)

            valid_moves = self.get_valid_moves(starting_square)

            temp = True

            if ending_square in valid_moves:
                moved_to_piece = self.get_piece(next_square_row, next_square_col)
                if moving_piece.get_name() is "k":
                    if moving_piece.is_player(Player.PLAYER_1):
                        if moved_to_piece == Player.EMPTY and next_square_col == 1 and self.king_can_castle_left(
                                moving_piece.get_player()):
                            move = chess_move(starting_square, ending_square, self, self._is_check)
                            move.castling_move((0, 0), (0, 2), self)
                            self.move_log.append(move)

                            # move rook
                            self.get_piece(0, 0).change_col_number(2)

                            self.board[0][2] = self.board[0][0]
                            self.board[0][0] = Player.EMPTY

                            self.white_king_can_castle[0] = False
                            self.white_king_can_castle[1] = False

                        elif moved_to_piece == Player.EMPTY and next_square_col == 5 and self.king_can_castle_right(
                                moving_piece.get_player()):
                            move = chess_move(starting_square, ending_square, self, self._is_check)
                            move.castling_move((0, 7), (0, 4), self)
                            self.move_log.append(move)
                            # move rook
                            self.get_piece(0, 7).change_col_number(4)

                            self.board[0][4] = self.board[0][7]
                            self.board[0][7] = Player.EMPTY

                            self.white_king_can_castle[0] = False
                            self.white_king_can_castle[2] = False
                        else:
                            move = chess_move(starting_square, ending_square, self, self._is_check)
                            self.move_log.append(move)
                            self.white_king_can_castle[0] = False
                        self._white_king_location = (next_square_row, next_square_col)
                    else:
                        if moved_to_piece == Player.EMPTY and next_square_col == 1 and self.king_can_castle_left(
                                moving_piece.get_player()):
                            move = chess_move(starting_square, ending_square, self, self._is_check)
                            move.castling_move((7, 0), (7, 2), self)
                            self.move_log.append(move)

                            self.get_piece(7, 0).change_col_number(2)
                            # move rook
                            self.board[7][2] = self.board[7][0]
                            self.board[7][0] = Player.EMPTY

                            self.black_king_can_castle[0] = False
                            self.black_king_can_castle[1] = False
                        elif moved_to_piece == Player.EMPTY and next_square_col == 5 and self.king_can_castle_right(
                                moving_piece.get_player()):
                            move = chess_move(starting_square, ending_square, self, self._is_check)
                            move.castling_move((7, 7), (7, 4), self)
                            self.move_log.append(move)

                            self.get_piece(0, 7).change_col_number(4)

                            # move rook
                            self.board[7][4] = self.board[7][7]
                            self.board[7][7] = Player.EMPTY

                            self.black_king_can_castle[0] = False
                            self.black_king_can_castle[2] = False
                        else:
                            move = chess_move(starting_square, ending_square, self, self._is_check)
                            self.move_log.append(move)
                            self.black_king_can_castle[0] = False
                        self._black_king_location = (next_square_row, next_square_col)
                        # self.can_en_passant_bool = False  WHAT IS THIS
                elif moving_piece.get_name() is "r":
                    if moving_piece.is_player(Player.PLAYER_1) and current_square_col == 0:
                        self.white_king_can_castle[1] = False
                    elif moving_piece.is_player(Player.PLAYER_1) and current_square_col == 7:
                        self.white_king_can_castle[2] = False
                    elif moving_piece.is_player(Player.PLAYER_2) and current_square_col == 0:
                        self.white_king_can_castle[1] = False
                    elif moving_piece.is_player(Player.PLAYER_2) and current_square_col == 7:
                        self.white_king_can_castle[2] = False
                    self.move_log.append(chess_move(starting_square, ending_square, self, self._is_check))
                    self.can_en_passant_bool = False
                # Add move class here
                elif moving_piece.get_name() is "p":
                    # Promoting white pawn
                    if moving_piece.is_player(Player.PLAYER_1) and next_square_row == 7:
                        # print("promoting white pawn")
                        if is_ai:
                            self.promote_pawn_ai(starting_square, moving_piece, ending_square)
                        else:
                            self.promote_pawn(starting_square, moving_piece, ending_square)
                        temp = False
                    # Promoting black pawn
                    elif moving_piece.is_player(Player.PLAYER_2) and next_square_row == 0:
                        # print("promoting black pawn")
                        if is_ai:
                            self.promote_pawn_ai(starting_square, moving_piece, ending_square)
                        else:
                            self.promote_pawn(starting_square, moving_piece, ending_square)
                        temp = False
                    # Moving pawn forward by two
                    # Problem with Pawn en passant ai
                    elif abs(next_square_row - current_square_row) == 2 and current_square_col == next_square_col:
                        # print("move pawn forward")
                        self.move_log.append(chess_move(starting_square, ending_square, self, self._is_check))
                        # self.can_en_passant_bool = True
                        self._en_passant_previous = (next_square_row, next_square_col)
                    # en passant
                    elif abs(next_square_row - current_square_row) == 1 and abs(
                            current_square_col - next_square_col) == 1 and \
                            self.can_en_passant(current_square_row, current_square_col):
                        # print("en passant")
                        if moving_piece.is_player(Player.PLAYER_1):
                            move = chess_move(starting_square, ending_square, self, self._is_check)
                            move.en_passant_move(self.board[next_square_row - 1][next_square_col],
                                                 (next_square_row - 1, next_square_col))
                            self.move_log.append(move)
                            self.board[next_square_row - 1][next_square_col] = Player.EMPTY
                        else:
                            move = chess_move(starting_square, ending_square, self, self._is_check)
                            move.en_passant_move(self.board[next_square_row + 1][next_square_col],
                                                 (next_square_row + 1, next_square_col))
                            self.move_log.append(move)
                            self.board[next_square_row + 1][next_square_col] = Player.EMPTY
                    # moving forward by one or taking a piece
                    else:
                        self.move_log.append(chess_move(starting_square, ending_square, self, self._is_check))
                        self.can_en_passant_bool = False
                else:
                    self.move_log.append(chess_move(starting_square, ending_square, self, self._is_check))
                    self.can_en_passant_bool = False

                if temp:
                    moving_piece.change_row_number(next_square_row)
                    moving_piece.change_col_number(next_square_col)
                    self.board[next_square_row][next_square_col] = self.board[current_square_row][current_square_col]
                    self.board[current_square_row][current_square_col] = Player.EMPTY

                self.white_turn = not self.white_turn

            else:
                pass

    # true if white, false if black
    def whose_turn(self):
        return self.white_turn

    '''
    check for immediate check
    - check 8 directions and 8 knight squares
    check for pins
    - whatever blocked from above is a pin
    
     - if immediate check, change check value to true
     - list valid moves to prevent check but not remove pin
     - if there are no valid moves to prevent check, checkmate
    '''

    def check_for_check(self, king_location, player):
        # self._is_check = False
        _checks = []
        _pins = []
        _pins_check = []

        king_location_row = king_location[0]
        king_location_col = king_location[1]

        _up = 1
        _down = 1
        _left = 1
        _right = 1

        # Left of the king
        _possible_pin = ()
        while king_location_col - _left >= 0 and self.get_piece(king_location_row,
                                                                king_location_col - _left) is not None:
            if self.is_valid_piece(king_location_row, king_location_col - _left) and \
                    self.get_piece(king_location_row, king_location_col - _left).is_player(player) and \
                    self.get_piece(king_location_row, king_location_col - _left).get_name() is not "k":
                if not _possible_pin:
                    _possible_pin = (king_location_row, king_location_col - _left)
                else:
                    break
            elif self.is_valid_piece(king_location_row, king_location_col - _left) and \
                    not self.get_piece(king_location_row, king_location_col - _left).is_player(player):
                if _possible_pin:
                    temp = self.board[_possible_pin[0]][_possible_pin[1]]
                    self.board[_possible_pin[0]][_possible_pin[1]] = Player.EMPTY
                    if (king_location_row, king_location_col) in self.get_piece(king_location_row,
                                                                                king_location_col - _left).get_valid_piece_takes(
                            self):
                        _pins.append(_possible_pin)
                        _pins_check.append((king_location_row, king_location_col - _left))
                    self.board[_possible_pin[0]][_possible_pin[1]] = temp
                else:
                    if (king_location_row, king_location_col) in self.get_piece(king_location_row,
                                                                                king_location_col - _left).get_valid_piece_takes(
                            self):
                        # self._is_check = True
                        _checks.append((king_location_row, king_location_col - _left))
                break
            _left += 1

        # right of the king
        _possible_pin = ()
        while king_location_col + _right < 8 and self.get_piece(king_location_row,
                                                                king_location_col + _right) is not None:
            if self.is_valid_piece(king_location_row, king_location_col + _right) and \
                    self.get_piece(king_location_row, king_location_col + _right).is_player(player) and \
                    self.get_piece(king_location_row, king_location_col + _right).get_name() is not "k":
                if not _possible_pin:
                    _possible_pin = (king_location_row, king_location_col + _right)
                else:
                    break
            elif self.is_valid_piece(king_location_row, king_location_col + _right) and \
                    not self.get_piece(king_location_row, king_location_col + _right).is_player(player):
                if _possible_pin:
                    temp = self.board[_possible_pin[0]][_possible_pin[1]]
                    self.board[_possible_pin[0]][_possible_pin[1]] = Player.EMPTY
                    if (king_location_row, king_location_col) in self.get_piece(king_location_row,
                                                                                king_location_col + _right).get_valid_piece_takes(
                            self):
                        _pins.append(_possible_pin)
                        _pins_check.append((king_location_row, king_location_col + _right))
                    self.board[_possible_pin[0]][_possible_pin[1]] = temp
                else:
                    if (king_location_row, king_location_col) in self.get_piece(king_location_row,
                                                                                king_location_col + _right).get_valid_piece_takes(
                            self):
                        # self._is_check = True
                        _checks.append((king_location_row, king_location_col + _right))
                break
            _right += 1

        # below the king
        _possible_pin = ()
        while king_location_row + _down < 8 and self.get_piece(king_location_row + _down,
                                                               king_location_col) is not None:
            if self.is_valid_piece(king_location_row + _down, king_location_col) and \
                    self.get_piece(king_location_row + _down, king_location_col).is_player(player) and \
                    self.get_piece(king_location_row + _down, king_location_col).get_name() is not "k":
                if not _possible_pin:
                    _possible_pin = (king_location_row + _down, king_location_col)
                else:
                    break
            elif self.is_valid_piece(king_location_row + _down, king_location_col) and \
                    not self.get_piece(king_location_row + _down, king_location_col).is_player(player):
                if _possible_pin:
                    temp = self.board[_possible_pin[0]][_possible_pin[1]]
                    self.board[_possible_pin[0]][_possible_pin[1]] = Player.EMPTY
                    if (king_location_row, king_location_col) in self.get_piece(king_location_row + _down,
                                                                                king_location_col).get_valid_piece_takes(
                            self):
                        _pins.append(_possible_pin)
                        _pins_check.append((king_location_row + _down, king_location_col))
                    self.board[_possible_pin[0]][_possible_pin[1]] = temp
                else:
                    if (king_location_row, king_location_col) in self.get_piece(king_location_row + _down,
                                                                                king_location_col).get_valid_piece_takes(
                        self):
                        # self._is_check = True
                        _checks.append((king_location_row + _down, king_location_col))
                break
            _down += 1

        # above the king
        _possible_pin = ()
        while king_location_row - _up >= 0 and self.get_piece(king_location_row - _up, king_location_col) is not None:
            if self.is_valid_piece(king_location_row - _up, king_location_col) and \
                    self.get_piece(king_location_row - _up, king_location_col).is_player(player) and \
                    self.get_piece(king_location_row - _up, king_location_col).get_name() is not "k":
                if not _possible_pin:
                    _possible_pin = (king_location_row - _up, king_location_col)
                else:
                    break
            elif self.is_valid_piece(king_location_row - _up, king_location_col) and \
                    not self.get_piece(king_location_row - _up, king_location_col).is_player(player):
                if _possible_pin:
                    temp = self.board[_possible_pin[0]][_possible_pin[1]]
                    self.board[_possible_pin[0]][_possible_pin[1]] = Player.EMPTY
                    if (king_location_row, king_location_col) in self.get_piece(king_location_row - _up,
                                                                                king_location_col).get_valid_piece_takes(
                            self):
                        _pins.append(_possible_pin)
                        _pins_check.append((king_location_row - _up, king_location_col))
                    self.board[_possible_pin[0]][_possible_pin[1]] = temp
                else:
                    if (king_location_row, king_location_col) in self.get_piece(king_location_row - _up,
                                                                                king_location_col).get_valid_piece_takes(
                            self):
                        # self._is_check = True
                        _checks.append((king_location_row - _up, king_location_col))
                break
            _up += 1

        # left up
        _up = 1
        _left = 1
        _possible_pin = ()
        while king_location_col - _left >= 0 and king_location_row - _up >= 0 and \
                self.get_piece(king_location_row - _up, king_location_col - _left) is not None:
            if self.is_valid_piece(king_location_row - _up, king_location_col - _left) and \
                    self.get_piece(king_location_row - _up, king_location_col - _left).is_player(player) and \
                    self.get_piece(king_location_row - _up, king_location_col - _left).get_name() is not "k":
                if not _possible_pin:
                    _possible_pin = (king_location_row - _up, king_location_col - _left)
                else:
                    break
            elif self.is_valid_piece(king_location_row - _up, king_location_col - _left) and \
                    not self.get_piece(king_location_row - _up, king_location_col - _left).is_player(player):
                if _possible_pin:
                    temp = self.board[_possible_pin[0]][_possible_pin[1]]
                    self.board[_possible_pin[0]][_possible_pin[1]] = Player.EMPTY
                    if (king_location_row, king_location_col) in self.get_piece(king_location_row - _up,
                                                                                king_location_col - _left).get_valid_piece_takes(
                            self):
                        _pins.append(_possible_pin)
                        _pins_check.append((king_location_row - _up, king_location_col - _left))
                    self.board[_possible_pin[0]][_possible_pin[1]] = temp
                else:
                    if (king_location_row, king_location_col) in self.get_piece(king_location_row - _up,
                                                                                king_location_col - _left).get_valid_piece_takes(
                        self):
                        # self._is_check = True
                        _checks.append((king_location_row - _up, king_location_col - _left))
                break
            _left += 1
            _up += 1

        # right up
        _up = 1
        _right = 1
        _possible_pin = ()
        while king_location_col + _right < 8 and king_location_row - _up >= 0 and \
                self.get_piece(king_location_row - _up, king_location_col + _right) is not None:
            if self.is_valid_piece(king_location_row - _up, king_location_col + _right) and \
                    self.get_piece(king_location_row - _up, king_location_col + _right).is_player(player) and \
                    self.get_piece(king_location_row - _up, king_location_col + _right).get_name() is not "k":
                if not _possible_pin:
                    _possible_pin = (king_location_row - _up, king_location_col + _right)
                else:
                    break
            elif self.is_valid_piece(king_location_row - _up, king_location_col + _right) and \
                    not self.get_piece(king_location_row - _up, king_location_col + _right).is_player(player):
                if _possible_pin:
                    temp = self.board[_possible_pin[0]][_possible_pin[1]]
                    self.board[_possible_pin[0]][_possible_pin[1]] = Player.EMPTY
                    if (king_location_row, king_location_col) in self.get_piece(king_location_row - _up,
                                                                                king_location_col + _right).get_valid_piece_takes(
                            self):
                        _pins.append(_possible_pin)
                        _pins_check.append((king_location_row - _up, king_location_col + _right))
                    self.board[_possible_pin[0]][_possible_pin[1]] = temp
                else:
                    if (king_location_row, king_location_col) in self.get_piece(king_location_row - _up,
                                                                                king_location_col + _right).get_valid_piece_takes(
                        self):
                        # self._is_check = True
                        _checks.append((king_location_row - _up, king_location_col + _right))
                break
            _right += 1
            _up += 1

        # left down
        _down = 1
        _left = 1
        _possible_pin = ()
        while king_location_col - _left >= 0 and king_location_row + _down < 8 and \
                self.get_piece(king_location_row + _down, king_location_col - _left) is not None:
            if self.is_valid_piece(king_location_row + _down, king_location_col - _left) and \
                    self.get_piece(king_location_row + _down, king_location_col - _left).is_player(player) and \
                    self.get_piece(king_location_row + _down, king_location_col - _left).get_name() is not "k":
                if not _possible_pin:
                    _possible_pin = (king_location_row + _down, king_location_col - _left)
                else:
                    break
            elif self.is_valid_piece(king_location_row + _down, king_location_col - _left) and \
                    not self.get_piece(king_location_row + _down, king_location_col - _left).is_player(player):
                if _possible_pin:
                    temp = self.board[_possible_pin[0]][_possible_pin[1]]
                    self.board[_possible_pin[0]][_possible_pin[1]] = Player.EMPTY
                    if (king_location_row, king_location_col) in self.get_piece(king_location_row + _down,
                                                                                king_location_col - _left).get_valid_piece_takes(
                            self):
                        _pins.append(_possible_pin)
                        _pins_check.append((king_location_row + _down, king_location_col - _left))
                    self.board[_possible_pin[0]][_possible_pin[1]] = temp
                else:
                    if (king_location_row, king_location_col) in self.get_piece(king_location_row + _down,
                                                                                king_location_col - _left).get_valid_piece_takes(
                        self):
                        # self._is_check = True
                        _checks.append((king_location_row + _down, king_location_col - _left))
                break
            _left += 1
            _down += 1

        # right down
        _down = 1
        _right = 1
        _possible_pin = ()
        while king_location_col + _right < 8 and king_location_row + _down < 8 and \
                self.get_piece(king_location_row + _down, king_location_col + _right) is not None:
            if self.is_valid_piece(king_location_row + _down, king_location_col + _right) and \
                    self.get_piece(king_location_row + _down, king_location_col + _right).is_player(player) and \
                    self.get_piece(king_location_row + _down, king_location_col + _right).get_name() is not "k":
                if not _possible_pin:
                    _possible_pin = (king_location_row + _down, king_location_col + _right)
                else:
                    break
            elif self.is_valid_piece(king_location_row + _down, king_location_col + _right) and \
                    not self.get_piece(king_location_row + _down, king_location_col + _right).is_player(player):
                if _possible_pin:
                    temp = self.board[_possible_pin[0]][_possible_pin[1]]
                    self.board[_possible_pin[0]][_possible_pin[1]] = Player.EMPTY
                    if (king_location_row, king_location_col) in self.get_piece(king_location_row + _down,
                                                                                king_location_col + _right).get_valid_piece_takes(
                            self):
                        _pins.append(_possible_pin)
                        _pins_check.append((king_location_row + _down, king_location_col + _right))
                    self.board[_possible_pin[0]][_possible_pin[1]] = temp
                else:
                    if (king_location_row, king_location_col) in self.get_piece(king_location_row + _down,
                                                                                king_location_col + _right).get_valid_piece_takes(
                        self):
                        # self._is_check = True
                        _checks.append((king_location_row + _down, king_location_col + _right))
                break
            _right += 1
            _down += 1

        # knights
        row_change = [-2, -2, -1, -1, +1, +1, +2, +2]
        col_change = [-1, +1, -2, +2, -2, +2, +1, -1]
        for i in range(0, 8):
            if self.is_valid_piece(king_location_row + row_change[i], king_location_col + col_change[i]) and \
                    not self.get_piece(king_location_row + row_change[i], king_location_col + col_change[i]).is_player(
                        player):
                if (king_location_row, king_location_col) in self.get_piece(king_location_row + row_change[i],
                                                                            king_location_col + col_change[
                                                                                i]).get_valid_piece_takes(self):
                    # self._is_check = True
                    _checks.append((king_location_row + row_change[i], king_location_col + col_change[i]))
        # print([_checks, _pins, _pins_check])
        return [_checks, _pins, _pins_check]


class chess_move():
    def __init__(self, starting_square, ending_square, game_state, in_check):
        self.starting_square_row = starting_square[0]
        self.starting_square_col = starting_square[1]
        self.moving_piece = game_state.get_piece(self.starting_square_row, self.starting_square_col)
        self.in_check = in_check

        self.ending_square_row = ending_square[0]
        self.ending_square_col = ending_square[1]
        if game_state.is_valid_piece(self.ending_square_row, self.ending_square_col):
            self.removed_piece = game_state.get_piece(self.ending_square_row, self.ending_square_col)
        else:
            self.removed_piece = Player.EMPTY

        self.castled = False
        self.rook_starting_square = None
        self.rook_ending_square = None
        self.moving_rook = None

        self.pawn_promoted = False
        self.replacement_piece = None

        self.en_passaned = False
        self.en_passant_eaten_piece = None
        self.en_passant_eaten_square = None

    def castling_move(self, rook_starting_square, rook_ending_square, game_state):
        self.castled = True
        self.rook_starting_square = rook_starting_square
        self.rook_ending_square = rook_ending_square
        self.moving_rook = game_state.get_piece(rook_starting_square[0], rook_starting_square[1])

    def pawn_promotion_move(self, new_piece):
        self.pawn_promoted = True
        self.replacement_piece = new_piece

    def en_passant_move(self, eaten_piece, eaten_piece_square):
        self.en_passaned = True
        self.en_passant_eaten_piece = eaten_piece
        self.en_passant_eaten_square = eaten_piece_square

    def get_moving_piece(self):
        return self.moving_piece