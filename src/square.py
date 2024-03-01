from dataclasses import dataclass


@dataclass
class Square:

    square_index: int

    def get_square_index(self):
        return self.square_index

    def get_square_name(self):
        pass

    def get_inverted_square_index(self):
        return 63 - self.square_index

    def get_square_coordinates(self):
        pass
