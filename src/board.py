from dataclasses import dataclass
import chess


@dataclass
class Board:

    chess_board = chess.Board
    # indexed by (a, 3)

    def __getitem__(self, item):
        raise


class Position():
    x: int
    y: int

    def up(self, steps=1):
        self.y += steps

    def right(self, steps=1):
        self.x += steps
