
import chess

from src.stockfish_features import (ExtractNonPawnMaterial, mobility_area,
                                    mobility_eg, mobility_mg, pawnless_flank,
                                    pawnless_flank_colored, piece_value_eg,
                                    piece_value_mg, psqt_eg, psqt_mg,
                                    strength_square)


def test_non_pawn_material_starting_position():
    board = chess.Board()
    assert ExtractNonPawnMaterial.extract_feature(board, is_midgame=True, color=chess.WHITE) == 0


def test_non_pawn_material_no_queen():
    board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
    assert ExtractNonPawnMaterial.extract_feature(board, is_midgame=True, color=chess.WHITE) == -2538


def test_non_pawn_material_random_position():
    board = chess.Board("r1bqk1n1/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
    assert ExtractNonPawnMaterial.extract_feature(board, is_midgame=True, color=chess.WHITE) == 344


def test_piece_value_mg_starting_position():
    board = chess.Board()
    assert piece_value_mg(board) == 0


def test_piece_value_mg_no_queen():
    board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
    assert piece_value_mg(board) == -2786


def test_piece_value_mg_random_position():
    board = chess.Board("r1bqk1n1/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
    assert piece_value_mg(board) == 96


def test_piece_value_eg_starting_position():
    board = chess.Board()
    assert piece_value_eg(board) == 0


def test_piece_value_eg_no_queen():
    board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
    assert piece_value_eg(board) == -3094


def test_piece_value_eg_random_position():
    board = chess.Board("r1bqk1n1/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
    assert piece_value_eg(board) == 55


def test_psqt_bonus_mg_starting_position():
    board = chess.Board()
    assert psqt_mg(board) == 0


def test_psqt_bonus_mg_no_queen():
    board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
    assert psqt_mg(board) == -33


def test_psqt_bonus_mg_random_position():
    board = chess.Board("r1bqk1n1/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
    assert psqt_mg(board) == -164


def test_psqt_bonus_eg_starting_position():
    board = chess.Board()
    assert psqt_eg(board) == 0


def test_psqt_bonus_eg_no_queen():
    board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
    assert psqt_eg(board) == 16


def test_psqt_bonus_eg_random_position():
    board = chess.Board("r1bqk1n1/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
    assert psqt_eg(board) == -95


def test_mobility_area_starting_position():
    board = chess.Board()
    assert mobility_area(board) == 0


def test_mobility_area_no_queen():
    board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
    assert mobility_area(board) == 3


def test_mobility_area_random_position():
    board = chess.Board("r1bqk1n1/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
    assert mobility_area(board) == 3


def test_mobility_area_random_position_with_pins():
    board = chess.Board("b2rk1n1/p1p1pp2/pP1p2b1/1P1N1P1p/2qBK3/4B3/7P/RN2r2R w KQkq - 2 5")
    assert mobility_area(board) == -3


def test_mobility_mg_random_starting_position():
    board = chess.Board()
    assert mobility_mg(board) == -172


def test_mobility_mg_random_no_queen():
    board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
    assert mobility_mg(board) == -66


def test_mobility_mg_random_random_position():
    board = chess.Board("r1bqk1n1/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
    assert mobility_mg(board) == -66


def test_mobility_mg_random_position_with_pins():
    board = chess.Board("b2rk1n1/p1p1pp2/pP1p2b1/1P1N1P1p/2qBK3/4B3/7P/RN2r2R w KQkq - 2 5")
    assert mobility_mg(board) == -137


def test_mobility_eg_starting_position():
    board = chess.Board()
    assert mobility_eg(board) == -244


def test_mobility_eg_no_queen():
    board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
    assert mobility_eg(board) == -116


def test_mobility_eg_random_position():
    board = chess.Board("r1bqk1n1/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
    assert mobility_eg(board) == -116


def test_mobility_eg_random_position_with_pins():
    board = chess.Board("b2rk1n1/p1p1pp2/pP1p2b1/1P1N1P1p/2qBK3/4B3/7P/RN2r2R w KQkq - 2 5")
    assert mobility_eg(board) == -73


def test_pawnless_flank_colored_starting_position():
    board = chess.Board()
    assert pawnless_flank_colored(board) == 0


def test_pawnless_flank_colored_no_queen():
    board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
    assert pawnless_flank_colored(board) == 0


def test_pawnless_flank_colored_random_position():
    board = chess.Board("r1bqk1n1/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
    assert pawnless_flank_colored(board) == 0


def test_pawnless_flank_colored_random_position_with_pins():
    board = chess.Board("b2rk1n1/p1p1pp2/pP1p2b1/1P1N1P1p/2qBK3/4B3/7P/RN2r2R w KQkq - 2 5")
    assert pawnless_flank_colored(board) == 0


def test_pawnless_flank_colored_endgame():
    board = chess.Board("1k6/4pp1p/8/8/4B3/8/4PP1P/5K2 w - - 2 2")
    assert pawnless_flank_colored(board) == 0


def test_pawnless_flank_colored_endgame_black():
    board = chess.Board("1k6/4pp1p/8/8/4B3/8/4PP1P/5K2 w - - 2 2")
    assert pawnless_flank_colored(board, chess.BLACK) == 1


def test_pawnless_flank_starting_position():
    board = chess.Board()
    assert pawnless_flank(board) == 0


def test_pawnless_flank_no_queen():
    board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
    assert pawnless_flank(board) == 0


def test_pawnless_flank_random_position():
    board = chess.Board("r1bqk1n1/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
    assert pawnless_flank(board) == 0


def test_pawnless_flank_random_position_with_pins():
    board = chess.Board("b2rk1n1/p1p1pp2/pP1p2b1/1P1N1P1p/2qBK3/4B3/7P/RN2r2R w KQkq - 2 5")
    assert pawnless_flank(board) == 0


def test_pawnless_flank_endgame():
    board = chess.Board("1k6/4pp1p/8/8/4B3/8/4PP1P/5K2 w - - 2 2")
    assert pawnless_flank(board) == 1


def test_pawnless_flank_endgame_2():
    board = chess.Board("6k1/4pp1p/8/8/4B3/8/4PP1P/1K6 w - - 2 2")
    assert pawnless_flank(board) == -1


def test_strength_square_starting_position():
    board = chess.Board()
    assert strength_square(board) == 0


def test_strength_square_no_queen():
    board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
    assert strength_square(board) == 836


def test_strength_square_random_position():
    board = chess.Board("r1bqk1n1/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
    assert strength_square(board) == 836


def test_strength_square_random_position_with_pins():
    board = chess.Board("b2rk1n1/p1p1pp2/pP1p2b1/1P1N1P1p/2qBK3/4B3/7P/RN2r2R w KQkq - 2 5")
    assert strength_square(board) == 250


def test_strength_square_endgame():
    board = chess.Board("1k6/4pp1p/8/8/4B3/8/4PP1P/5K2 w - - 2 2")
    assert strength_square(board) == 0


def test_strength_square_endgame_2():
    board = chess.Board("6k1/4pp1p/8/8/4B3/8/4PP1P/1K6 w - - 2 2")
    assert strength_square(board) == 0
