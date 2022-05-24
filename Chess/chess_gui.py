import chess_engine
import pygame as py
import ai_engine_better
import ai_engine
import random_engine
import ai_engine_ml
from enums import Player

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}
colors = [py.Color("white"), py.Color("gray")]


def load_images():
    for p in Player.PIECES:
        IMAGES[p] = py.transform.scale(py.image.load(
            "images/" + p + ".png"), (SQ_SIZE, SQ_SIZE))


def draw_game_state(screen, game_state, valid_moves, square_selected):
    draw_squares(screen)
    highlight_square(screen, game_state, valid_moves, square_selected)
    draw_pieces(screen, game_state)


def draw_squares(screen):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r + c) % 2]
            py.draw.rect(screen, color, py.Rect(
                c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def draw_pieces(screen, game_state):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = game_state.get_piece(r, c)
            if piece is not None and piece != Player.EMPTY:
                screen.blit(IMAGES[piece.get_player() + "_" + piece.get_name()],
                            py.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def highlight_square(screen, game_state, valid_moves, square_selected):
    if square_selected != () and game_state.is_valid_piece(square_selected[0], square_selected[1]):
        row = square_selected[0]
        col = square_selected[1]

        if (game_state.whose_turn() and game_state.get_piece(row, col).is_player(Player.PLAYER_1)) or \
                (not game_state.whose_turn() and game_state.get_piece(row, col).is_player(Player.PLAYER_2)):
            s = py.Surface((SQ_SIZE, SQ_SIZE))
            s.set_alpha(100)
            s.fill(py.Color("blue"))
            screen.blit(s, (col * SQ_SIZE, row * SQ_SIZE))

            s.fill(py.Color("green"))

            for move in valid_moves:
                screen.blit(s, (move[1] * SQ_SIZE, move[0] * SQ_SIZE))


def main():
    setting = ""

    while True:
        try:
            number_of_players = input(
                "0: 2 bot\n1: 1 bot\n2: Radom\n3: 2 bot(1 Machine_Learning - 1 Random)\nSelect play mode: ")

            if int(number_of_players) == 0:
                number_of_players = 0
                while True:
                    setting = input(
                        "What color do you want PRO play?\nSelect (w or b): ")
                    if setting == "w" or setting == "b":
                        break
                    else:
                        print("Enter w or b.\n")
                break
            elif int(number_of_players) == 1:
                number_of_players = 1
                setting = "b"
                print("You are black")
                break
            elif int(number_of_players) == 2:
                number_of_players = 2
                while True:
                    setting = input(
                        "What color do you want PRO play?\nSelect (w or b): ")
                    if setting == "w" or setting == "b":
                        break
                    else:
                        print("Enter w or b.\n")
                break
            elif int(number_of_players) == 3:
                number_of_players = 3
                while True:
                    setting = input(
                        "What color do you want ML play?\nSelect (w or b): ")
                    if setting == "w" or setting == "b":
                        break
                    else:
                        print("Enter w or b.\n")
                break
            else:
                print("Enter 0 or 1 or 2 or 3.\n")
        except ValueError:
            print("Enter 0 or 1 or 2 or 3.\n")

    py.init()
    screen = py.display.set_mode((WIDTH, HEIGHT))
    clock = py.time.Clock()
    load_images()
    running = True
    square_selected = ()
    player_clicks = []
    valid_moves = []
    game_over = False

    pro = ai_engine_better.chess_ai()
    noob = ai_engine.chess_ai()
    rand = random_engine.chess_random()
    ml = ai_engine_ml.chess_ai()
    game_state = chess_engine.game_state()

    if setting == 'b' and number_of_players == 1:
        ai_move = ml.minimax_black(
            game_state, 1, -100000, 100000, True, Player.PLAYER_1)
        game_state.move_piece(ai_move[0], ai_move[1], True)

    while running:
        for e in py.event.get():
            if e.type == py.QUIT:
                running = False
            elif e.type == py.MOUSEBUTTONDOWN:
                if not game_over:
                    if number_of_players == 0 or number_of_players == 2:
                        if not game_over:
                            if setting == 'w':
                                ai_move = pro.minimax_black(
                                    game_state, 2, -100000, 100000, True, Player.PLAYER_1)
                                game_state.move_piece(
                                    ai_move[0], ai_move[1], True)

                                draw_game_state(
                                    screen, game_state, valid_moves, square_selected)
                                endgame = game_state.checkmate_stalemate_checker()
                                if endgame == 0:
                                    game_over = True
                                    draw_text(screen, "Black wins.")
                                    continue
                                elif endgame == 1:
                                    game_over = True
                                    draw_text(screen, "White wins.")
                                    continue
                                elif endgame == 2:
                                    game_over = True
                                    draw_text(screen, "Stalemate.")
                                    continue
                                clock.tick(MAX_FPS)
                                py.display.flip()

                                if number_of_players == 2:
                                    ai_move = rand.get_move(
                                        game_state, Player.PLAYER_2)
                                    game_state.move_piece(
                                        ai_move[0], ai_move[1], True)
                                else:
                                    ai_move = noob.minimax_white(
                                        game_state, 2, -100000, 100000, True, Player.PLAYER_2)
                                    game_state.move_piece(
                                        ai_move[0], ai_move[1], True)
                            elif setting == 'b':
                                if number_of_players == 2:
                                    ai_move = rand.get_move(
                                        game_state, Player.PLAYER_1)
                                    game_state.move_piece(
                                        ai_move[0], ai_move[1], True)
                                else:
                                    ai_move = noob.minimax_black(
                                        game_state, 2, -100000, 100000, True, Player.PLAYER_1)
                                    game_state.move_piece(
                                        ai_move[0], ai_move[1], True)

                                draw_game_state(
                                    screen, game_state, valid_moves, square_selected)
                                endgame = game_state.checkmate_stalemate_checker()
                                if endgame == 0:
                                    game_over = True
                                    draw_text(screen, "Black wins.")
                                    continue
                                elif endgame == 1:
                                    game_over = True
                                    draw_text(screen, "White wins.")
                                    continue
                                elif endgame == 2:
                                    game_over = True
                                    draw_text(screen, "Stalemate.")
                                    continue
                                clock.tick(MAX_FPS)
                                py.display.flip()
                                ai_move = pro.minimax_white(
                                    game_state, 2, -100000, 100000, True, Player.PLAYER_2)
                                game_state.move_piece(
                                    ai_move[0], ai_move[1], True)
                    elif number_of_players == 3:
                        if not game_over:
                            if setting == 'w':
                                ai_move = ml.minimax_black(
                                    game_state, 1, -100000, 100000, True, Player.PLAYER_1)
                                game_state.move_piece(
                                    ai_move[0], ai_move[1], True)

                                draw_game_state(
                                    screen, game_state, valid_moves, square_selected)
                                endgame = game_state.checkmate_stalemate_checker()
                                if endgame == 0:
                                    game_over = True
                                    draw_text(screen, "Black wins.")
                                    continue
                                elif endgame == 1:
                                    game_over = True
                                    draw_text(screen, "White wins.")
                                    continue
                                elif endgame == 2:
                                    game_over = True
                                    draw_text(screen, "Stalemate.")
                                    continue
                                clock.tick(MAX_FPS)
                                py.display.flip()
                                ai_move = rand.get_move(
                                    game_state, Player.PLAYER_2)
                                game_state.move_piece(
                                    ai_move[0], ai_move[1], True)
                            elif setting == 'b':
                                ai_move = rand.get_move(
                                    game_state, Player.PLAYER_1)
                                game_state.move_piece(
                                    ai_move[0], ai_move[1], True)

                                draw_game_state(
                                    screen, game_state, valid_moves, square_selected)
                                endgame = game_state.checkmate_stalemate_checker()
                                if endgame == 0:
                                    game_over = True
                                    draw_text(screen, "Black wins.")
                                    continue
                                elif endgame == 1:
                                    game_over = True
                                    draw_text(screen, "White wins.")
                                    continue
                                elif endgame == 2:
                                    game_over = True
                                    draw_text(screen, "Stalemate.")
                                    continue
                                clock.tick(MAX_FPS)
                                py.display.flip()
                                ai_move = ml.minimax_white(
                                    game_state, 1, -100000, 100000, True, Player.PLAYER_2)
                                game_state.move_piece(
                                    ai_move[0], ai_move[1], True)
                    else:
                        location = py.mouse.get_pos()
                        col = location[0] // SQ_SIZE
                        row = location[1] // SQ_SIZE
                        if square_selected == (row, col):
                            square_selected = ()
                            player_clicks = []
                        else:
                            square_selected = (row, col)
                            player_clicks.append(square_selected)
                        if len(player_clicks) == 2:
                            # this if is useless right now
                            if (player_clicks[1][0], player_clicks[1][1]) not in valid_moves:
                                square_selected = ()
                                player_clicks = []
                                valid_moves = []
                            else:
                                game_state.move_piece((player_clicks[0][0], player_clicks[0][1]),
                                                      (player_clicks[1][0], player_clicks[1][1]), False)
                                square_selected = ()
                                player_clicks = []
                                valid_moves = []

                                draw_game_state(
                                    screen, game_state, valid_moves, square_selected)
                                endgame = game_state.checkmate_stalemate_checker()
                                if endgame == 0:
                                    game_over = True
                                    draw_text(screen, "Black wins.")
                                    continue
                                elif endgame == 1:
                                    game_over = True
                                    draw_text(screen, "White wins.")
                                    continue
                                elif endgame == 2:
                                    game_over = True
                                    draw_text(screen, "Stalemate.")
                                    continue

                                if setting == 'w':
                                    ai_move = ml.minimax_white(
                                        game_state, 1, -100000, 100000, True, Player.PLAYER_2)
                                    game_state.move_piece(
                                        ai_move[0], ai_move[1], True)
                                elif setting == 'b':
                                    ai_move = ml.minimax_black(
                                        game_state, 1, -100000, 100000, True, Player.PLAYER_1)
                                    game_state.move_piece(
                                        ai_move[0], ai_move[1], True)
                        else:
                            valid_moves = game_state.get_valid_moves(
                                (row, col))
                            if valid_moves == None:
                                valid_moves = []

            elif e.type == py.KEYDOWN:
                if e.key == py.K_r:
                    game_over = False
                    game_state = chess_engine.game_state()
                    valid_moves = []
                    square_selected = ()
                    player_clicks = []
                    valid_moves = []
                elif e.key == py.K_u:
                    game_state.undo_move()
                    print(len(game_state.move_log))

        draw_game_state(screen, game_state, valid_moves, square_selected)

        endgame = game_state.checkmate_stalemate_checker()

        if endgame == 0:
            game_over = True
            draw_text(screen, "Black wins.")
        elif endgame == 1:
            game_over = True
            draw_text(screen, "White wins.")
        elif endgame == 2:
            game_over = True
            draw_text(screen, "Stalemate.")

        clock.tick(MAX_FPS)
        py.display.flip()


def draw_text(screen, text):
    font = py.font.SysFont("Helvitca", 32, True, False)
    text_object = font.render(text, False, py.Color("Black"))
    text_location = py.Rect(0, 0, WIDTH, HEIGHT).move(WIDTH / 2 - text_object.get_width() / 2,
                                                      HEIGHT / 2 - text_object.get_height() / 2)
    screen.blit(text_object, text_location)


if __name__ == "__main__":
    main()
