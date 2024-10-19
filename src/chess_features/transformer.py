
from src.chess_features.chess_features import (
    to_bit_attack_map,
    to_bit_defend_map,
    to_bitboard,
    to_chess_neighborhoods,
    to_fen,
    to_san,
    to_unified_neg_bitboard,
    to_valued_attack_map,
    to_valued_bitboard,
    to_valued_defend_map,
    to_white_moving,
)

transformation_mapping = {
    "bit_attack": to_bit_attack_map,
    "bit_defend": to_bit_defend_map,
    "bit": to_bitboard,
    "neighborhood": to_chess_neighborhoods,
    "fen": to_fen,
    "san": to_san,
    "bit_unified": to_unified_neg_bitboard,
    "valued_attack": to_valued_attack_map,
    "valued_unified": to_valued_bitboard,
    "valued_defend": to_valued_defend_map,
    "white_moving": to_white_moving
}

class ChessTransformer():
    def __init__(self, transformation_type) -> None:
        self.transformation_type = transformation_type
        self.transformation_function = transformation_mapping[transformation_type]

    def __call__(self, board):
        return self.transformation_function(board)

    def get_available_transformations(self):
        return list(transformation_mapping.keys())