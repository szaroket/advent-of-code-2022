# Advent of code 2022
# Day 2: Rock Paper Scissors
# https://adventofcode.com/2022/day/2

from enum import IntEnum

SHAPE_SEPARATOR = " "


class Points(IntEnum):
    LOSS = 0
    DRAW = 3
    WIN = 6
    X = 1
    Y = 2
    Z = 3


ROUND_RESULT = {
    ('A', 'X'): "DRAW",
    ('A', 'Y'): "WIN",
    ('A', 'Z'): "LOSS",
    ('B', 'X'): "LOSS",
    ('B', 'Y'): "DRAW",
    ('B', 'Z'): "WIN",
    ('C', 'X'): "WIN",
    ('C', 'Y'): "LOSS",
    ('C', 'Z'): "DRAW"
}

REQUIRED_SHAPE = {
    ('A', 'X'): "Z",
    ('A', 'Y'): "X",
    ('A', 'Z'): "Y",
    ('B', 'X'): "X",
    ('B', 'Y'): "Y",
    ('B', 'Z'): "Z",
    ('C', 'X'): "Y",
    ('C', 'Y'): "Z",
    ('C', 'Z'): "X"
}


def read_input() -> str:
    with open("input.txt", "r") as f:
        data = f.read()
    return data


def prepare_data(data: str) -> list:
    return [tuple(pair.split(SHAPE_SEPARATOR)) for pair in data.split("\n")]


def calculate_points_part1(rounds: list[tuple]) -> int:
    total_points = 0
    for one_round in rounds:
        total_points = total_points + Points[ROUND_RESULT[one_round]].value + Points[one_round[1]].value
    return total_points


def calculate_points_part2(rounds: list[tuple]) -> int:
    total_points = 0
    for one_round in rounds:
        shapes = (one_round[0], REQUIRED_SHAPE[one_round])
        total_points = total_points + Points[ROUND_RESULT[shapes]].value + Points[REQUIRED_SHAPE[one_round]].value
    return total_points


if __name__ == "__main__":
    input_data = read_input()
    prepared_data = prepare_data(input_data)
    part1_points = calculate_points_part1(prepared_data)
    print(f"Total score for part 1 is: {part1_points}")
    part2_points = calculate_points_part2(prepared_data)
    print(f"Total score for part 2 is: {part2_points}")
