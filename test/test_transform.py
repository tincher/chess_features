import chess
import chess.pgn
import numpy as np
from src.my_transform import (bitboard_to_bitvector, to_bitboard, to_chess_neighborhoods, to_fen, to_san,
                              to_unified_neg_bitboard, to_valued_bitboard, to_white_moving, to_valued_attack_map,
                              to_valued_defend_map, to_bit_defend_map, to_bit_attack_map)


def test_bitboard_to_bitvector():
    # prepare
    with open('./chess_features/test/test_files/expected_valued_bitboard.txt', 'r', encoding="utf-8") as f:
        data = f.read()
    data = data.replace('array', 'np.array')
    loaded_bitboard = eval(data)

    with open('./chess_features/test/test_files/expected_valued_vector.txt', 'r', encoding="utf-8") as f:
        data = f.read()
    data = data.replace('array', 'np.array')
    loaded_bitvector = eval(data)

    bitvector = bitboard_to_bitvector(loaded_bitboard)

    np.testing.assert_array_equal(loaded_bitvector, bitvector)


def test_to_fen():
    with open("./chess_features/test/test_files/expected_fen.txt", "r", encoding="utf-8") as fen_file:
        content = fen_file.readline().strip()
        board = chess.Board(content)
        created_fen = to_fen(board)
        assert content == created_fen


def test_to_valued_bitboard():
    board = chess.Board()
    bitboard = to_valued_bitboard(board)

    # load expected
    with open('./chess_features/test/test_files/expected_valued_bitboard.txt', 'r', encoding="utf-8") as f:
        data = f.read()
    data = data.replace('array', 'np.array')
    loaded_bitboard = eval(data)

    print(bitboard, loaded_bitboard)

    np.testing.assert_array_equal(bitboard, loaded_bitboard)


def test_to_white_moving():
    with open("./chess_features/test/test_files/expected_fen.txt", "r", encoding="utf-8") as fen_file:
        content = fen_file.readline().strip()
    board_black_to_move = chess.Board(content.replace("w", "b"))
    board_white_to_move = chess.Board(content)
    mirrored_black_to_move_board = board_black_to_move.copy()
    mirrored_black_to_move_board.mirror()

    assert to_white_moving(board_black_to_move) == mirrored_black_to_move_board
    assert to_white_moving(board_white_to_move) == board_white_to_move


def test_to_binary_bitboard():
    board = chess.Board()
    bitboard = to_bitboard(board)

    # load expected
    with open('./chess_features/test/test_files/expected_binary_bitboard.txt', 'r', encoding="utf-8") as f:
        data = f.read()
    data = data.replace('array', 'np.array')
    loaded_bitboard = eval(data)

    print(bitboard, loaded_bitboard)

    np.testing.assert_array_equal(bitboard, loaded_bitboard)


def test_to_unified_bitboard():
    board = chess.Board()
    bitboard = to_unified_neg_bitboard(board)

    # load expected
    with open('./chess_features/test/test_files/expected_unified_bitboard.txt', 'r', encoding="utf-8") as f:
        data = f.read()
    data = data.replace('array', 'np.array')
    loaded_bitboard = eval(data)

    print(bitboard, loaded_bitboard)

    np.testing.assert_array_equal(bitboard, loaded_bitboard)


def test_to_pgn():
    board = chess.Board()

    with open("./chess_features/test/test_files/fisher.pgn", "r", encoding="utf-8") as pgn_file:
        first_game = chess.pgn.read_game(pgn_file)

    with open("./chess_features/test/test_files/expected_san.txt", "r", encoding="utf-8") as expected_san_file:
        expected_san = expected_san_file.read()

    node = first_game
    while node.variations:
        move = node.variation(0).move
        board.push(move)
        node = node.variation(0)

    san = to_san(board)

    assert san == expected_san


def test_to_pos2vec():
    raise NotImplementedError


def test_to_bit_attack_map():
    board = chess.Board()
    attack_map = to_bit_attack_map(board)

    # load expected
    with open('./chess_features/test/test_files/expected_bit_attack_map.txt', 'r', encoding="utf-8") as f:
        data = f.read()
    data = data.replace('array', 'np.array')
    print(data)
    loaded_defend_map = eval(data)

    assert attack_map.shape == loaded_defend_map.shape
    np.testing.assert_array_equal(attack_map, loaded_defend_map)


def test_to_bit_defend_map():
    board = chess.Board()
    attack_map = to_bit_defend_map(board)

    # load expected
    with open('./chess_features/test/test_files/expected_bit_defend_map.txt', 'r', encoding="utf-8") as f:
        data = f.read()
    data = data.replace('array', 'np.array')
    print(data)
    loaded_defend_map = eval(data)

    assert attack_map.shape == loaded_defend_map.shape
    np.testing.assert_array_equal(attack_map, loaded_defend_map)


def test_to_valued_attack_map():
    board = chess.Board()
    attack_map = to_valued_attack_map(board)

    # load expected
    with open('./chess_features/test/test_files/expected_valued_attack_map.txt', 'r', encoding="utf-8") as f:
        data = f.read()
    data = data.replace('array', 'np.array')
    print(data)
    loaded_defend_map = eval(data)

    assert attack_map.shape == loaded_defend_map.shape
    np.testing.assert_array_equal(attack_map, loaded_defend_map)


def test_to_valued_defend_map():
    board = chess.Board()
    attack_map = to_valued_defend_map(board)

    # load expected
    with open('./chess_features/test/test_files/expected_valued_defend_map.txt', 'r', encoding="utf-8") as f:
        data = f.read()
    data = data.replace('array', 'np.array')
    print(data)
    loaded_defend_map = eval(data)

    assert attack_map.shape == loaded_defend_map.shape
    np.testing.assert_array_equal(attack_map, loaded_defend_map)


def test_to_chess_neighborhood():
    board = chess.Board()
    neighborhood = to_chess_neighborhoods(board)
    assert neighborhood.shape == (64, 17)

    with open('./chess_features/test/test_files/expected_chess_neighborhood.txt', 'r', encoding="utf-8") as f:
        data = f.read()
    data = data.replace('array', 'np.array')
    loaded_neighborhood = eval(data)

    np.testing.assert_array_equal(neighborhood, loaded_neighborhood)


def test_to_stockfish_representation():
    raise NotImplementedError