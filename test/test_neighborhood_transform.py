import chess

from src.neighborhood_transform import get_horse_neighbor, get_file_rank_neighbor, get_diagonal_neighbor, get_neighborhood
from src.my_transform import to_valued_bitboard
import numpy as np


class TestChessNeighborhoods:
    @classmethod
    def setup_class(cls):
        board = chess.Board("rnbqkb1r/ppppp2p/6p1/3n4/3R4/8/8/4K3 b Qkq - 3 4")
        valued_board = to_valued_bitboard(board)
        valued_board[-6:] = -valued_board[-6:]
        valued_board = np.sum(valued_board, axis=0)
        cls.board = valued_board

    def test_get_horse_neighbors(self):
        assert get_horse_neighbor(self.board, 2, 1, True, True, True) == -3
        assert get_horse_neighbor(self.board, 2, 1, True, True, False) == 0
        assert get_horse_neighbor(self.board, 2, 1, True, False, True) == 0
        assert get_horse_neighbor(self.board, 2, 1, True, False, False) == 0
        assert get_horse_neighbor(self.board, 2, 1, False, True, True) == 0
        assert get_horse_neighbor(self.board, 2, 1, False, True, False) == -500
        assert get_horse_neighbor(self.board, 2, 1, False, False, True) == 0
        assert get_horse_neighbor(self.board, 2, 1, False, False, False) == -5

    def test_get_file_rank_neighbor(self):
        assert get_file_rank_neighbor(self.board, 2, 1, 1, True) == 0
        assert get_file_rank_neighbor(self.board, 2, 1, 1, False) == -1
        assert get_file_rank_neighbor(self.board, 2, 1, -1, True) == -3
        assert get_file_rank_neighbor(self.board, 2, 1, -1, False) == -1

    def test_get_diagnoal_neighbor(self):
        assert get_diagonal_neighbor(self.board, 2, 1, 1, 1) == 0
        assert get_diagonal_neighbor(self.board, 2, 1, 1, -1) == 0
        assert get_diagonal_neighbor(self.board, 2, 1, -1, 1) == -9
        assert get_diagonal_neighbor(self.board, 2, 1, -1, -1) == -3

    def test_get_neighborhood_unordered(self):
        neighborhood = get_neighborhood(self.board, 2, 1, clockwise=False)
        np.testing.assert_equal(neighborhood, [-1, -3, 0, 0, 0, 0, -500, 0, -5, 0, -1, -3, -1, 0, 0, -9, -3])

    def test_get_neighborhood_clockwise(self):
        neighborhood = get_neighborhood(self.board, 2, 1, clockwise=True)
        np.testing.assert_equal(neighborhood, [-1, -1, -9, -3, -3, -1, 0, 0, 0, 0, -500, 0, 0, -5, 0, 0, -3])
