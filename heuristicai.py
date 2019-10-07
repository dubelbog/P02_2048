import random
import numpy

import game
import sys

# Author:				chrn (original by nneonneo)
# Date:				11.11.2016
# Description:			The logic of the AI to beat the game.
import gamectrl

UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3


def find_best_move(board):
    bestmove = -1

    # TODO: Build a heuristic agent on your own that is much better than the random agent. Your own agent don't have
    # TODO: to beat the game.
    print(board)

    sum_row_l = 0
    sum_row_r = 0
    sum_col_up = 0
    sum_col_down = 0

    result = [0 for x in range(4)]

    for row in board:
        row_reversed = list(reversed(row))
        for i in range(len(row) - 1):
            if row[i] == row[i + 1] and row[i] > 0:
                sum_row_l += 1
                row[i + 1] = 0
            if row_reversed[i] == row_reversed[i + 1] and row_reversed[i] > 0:
                sum_row_r += 1
                row_reversed[i + 1] = 0
    result[2] = sum_row_l
    result[3] = sum_row_r

    for col in board.T:
        col_reversed = list(reversed(col))
        for i in range(len(col) - 1):
            if col[i] == col[i + 1] and col[i] > 0:
                sum_col_up += 1
                col[i + 1] = 0
            if col_reversed[i] == col_reversed[i + 1] and col_reversed[i] > 0:
                sum_col_down += 1
                col_reversed[i + 1] = 0
    result[0] = sum_col_up
    result[1] = sum_col_down

    print("result: ", result)
    index = numpy.where(result == numpy.amax(result))

    if len(index[0]) == 4:
        bestmove = find_best_move_random_agent()
    else:
        bestmove = index[0][0]
    print("bestmove: ", bestmove)

    return bestmove


def find_best_move_random_agent():
    return random.choice([UP, DOWN, LEFT, RIGHT])


def execute_move(move, board):
    # move and return the grid without a new random tile . It won't affect the state of the game in the browser.

    if move == UP:
        return game.merge_up(board)
    elif move == DOWN:
        return game.merge_down(board)
    elif move == LEFT:
        return game.merge_left(board)
    elif move == RIGHT:
        return game.merge_right(board)
    else:
        sys.exit("No valid move")


def board_equals(board, newboard):
    # Check if two boards are equal

    return (newboard == board).all()

