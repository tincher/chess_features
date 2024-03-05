import numpy as np
from itertools import product


def get_square(board, changing, steady, y_changes=True):
    if y_changes:
        return board[changing][steady]
    else:
        return board[steady][changing]


def get_file_rank_neighbor(board, x, y, down_right_of_square=1, file_wise=True):
    steady_variable = x if file_wise else y
    changing_variable = y if file_wise else x

    max_distance = 7-changing_variable if down_right_of_square else changing_variable
    for distance in range(1, max_distance+1):
        if (neighbor_value := get_square(board, changing_variable+distance*down_right_of_square, steady_variable, file_wise)) != 0:
            return neighbor_value
    return 0


def get_horse_neighbor(board, x, y, under_square=True, right_of_square=True, closer_to_vertical=True):
    diffs = ((1, 2), (2, 1))[closer_to_vertical]
    diffs = (diffs[0] if under_square else - diffs[0], diffs[1] if right_of_square else - diffs[1])
    if (horse_y := y+diffs[0]) < 0 or horse_y > 7 or (horse_x := x+diffs[1]) < 0 or horse_x > 7:
        return 0
    return board[horse_y][horse_x]


def get_diagonal_neighbor(board, x, y, under_square=1, right_of_square=1):
    fn_matrix = [[min(x, y), min(7-x, y)],
                 [min(x, 7-y), min(7-x, 7-y)]]
    max_distance = fn_matrix[max(0, under_square)][max(0, right_of_square)]

    for distance in range(1, max_distance+1):
        if (neighbor_value := board[y+distance*under_square][x+distance*right_of_square]) != 0:
            return neighbor_value
    return 0


def get_neighborhood(board, x, y, clockwise=True):
    neighborhood = [board[y][x]]
    for under, right, close in product([True, False], repeat=3):
        neighborhood.append(get_horse_neighbor(board, x, y, under, right, close))
    for down_under, along_rank in product([1, -1], repeat=2):
        neighborhood.append(get_file_rank_neighbor(board, x, y, down_under, along_rank == 1))
    for under, right in product([1, -1], repeat=2):
        neighborhood.append(get_diagonal_neighbor(board, x, y, under, right))
    neighborhood = np.array(neighborhood)
    if clockwise:
        return neighborhood[[0, 10, 15, 11, 16, 12, 14, 9, 13, 2, 6, 5, 7,  8, 4, 3,  1]]
    return neighborhood
