# Advent of code 2022
# Day 2: Rock Paper Scissors
# https://adventofcode.com/2022/day/2

from enum import IntEnum


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


def read_input() -> list:
    with open("input.txt", "r") as f:
        data = f.read()
    return data


def prepare_data(data: str) -> list:
    return [tuple(pair.split(" ")) for pair in data.split("\n")]


def calculate_points(rounds: list) -> int:
    total_points = 0
    for one_round in rounds:
        total_points = total_points + Points[ROUND_RESULT[one_round]].value + Points[one_round[1]].value
    return total_points


if __name__ == "__main__":
    input_data = read_input()
    prepared_data = prepare_data(input_data)
    points = calculate_points(prepared_data)
    print(f"Total score is: {points}")
