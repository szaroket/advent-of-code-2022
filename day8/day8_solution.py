# Advent of code 2022
# Day 8: Treetop Tree House
# https://adventofcode.com/2022/day/8
import numpy as np
from numpy import ndarray


def read_input() -> str:
    with open("input.txt", "r") as f:
        data = f.read()
    return data


def prepare_data(data: str) -> ndarray:
    return np.array([list(map(int, tree)) for tree in data.split("\n")])


def calculate_visible_tree(trees: ndarray):
    visible_trees = 0
    for row_index, row in enumerate(trees):
        for col_index, col in enumerate(row):
            if (row_index != 0 and col_index != 0) and (
                row_index != len(trees) - 1 and col_index != len(row) - 1
            ):
                tree_high = trees[row_index][col_index]
                column = trees[:, col_index]
                visible_left = all(x < tree_high for x in row[:col_index])
                visible_right = all(x < tree_high for x in row[col_index + 1:])
                visible_down = all(x < tree_high for x in column[row_index + 1:])
                visible_up = all(x < tree_high for x in column[:row_index])
                if visible_down or visible_up or visible_right or visible_left:
                    visible_trees += 1
            else:
                visible_trees += 1
    print(f"Visible trees: {visible_trees}")


if __name__ == "__main__":
    input_data = read_input()
    trees_map = prepare_data(input_data)
    calculate_visible_tree(trees_map)
