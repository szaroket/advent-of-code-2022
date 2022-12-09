# Advent of code 2022
# Day 9: Rope Bridge
# https://adventofcode.com/2022/day/9
import math


def read_input() -> str:
    with open("input.txt", "r") as f:
        data = f.read()
    return data


def prepare_data(data: str) -> list[tuple]:
    return [tuple(move.split(" ")) for move in data.split("\n")]


def calculate_tail_move(moves: list[tuple], knots: int):
    rope = [[0, 0] for _ in range(knots)]
    tail_positions = {tuple(rope[0])}
    transitions = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
    for move in moves:
        direction = move[0]
        steps = int(move[1])
        for _ in range(steps):
            dx, dy = transitions[direction]
            rope[0][0] += dx
            rope[0][1] += dy
            for i in range(1, len(rope)):
                head = rope[i - 1]
                tail = rope[i]
                diff_x = head[0] - tail[0]
                diff_y = head[1] - tail[1]
                distance = math.sqrt(math.pow(diff_x, 2) + math.pow(diff_y, 2))
                if distance < 2:
                    continue
                if diff_x != 0:
                    tail[0] += 1 if diff_x > 0 else -1
                if diff_y != 0:
                    tail[1] += 1 if diff_y > 0 else -1
            tail_positions.add(tuple(rope[len(rope) - 1]))
    print(f"The tails for {knots} knots moved: {len(tail_positions)}")


if __name__ == "__main__":
    input_data = read_input()
    list_of_moves = prepare_data(input_data)
    calculate_tail_move(list_of_moves, 2)
    calculate_tail_move(list_of_moves, 10)
