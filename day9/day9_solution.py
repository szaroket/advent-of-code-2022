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


def perform_moves_part1(moves: list[tuple]):
    head = [0, 0]
    tail = [0, 0]
    tail_positions = {tuple(tail)}
    transitions = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
    for move in moves:
        direction = move[0]
        steps = int(move[1])
        for _ in range(steps):
            dx, dy = transitions[direction]
            head[0] += dx
            head[1] += dy
            diff_x = head[0] - tail[0]
            diff_y = head[1] - tail[1]
            distance = math.sqrt(math.pow(diff_x, 2) + math.pow(diff_y, 2))
            if distance < 2:
                continue
            if diff_x != 0:
                tail[0] += 1 if diff_x > 0 else -1
            if diff_y != 0:
                tail[1] += 1 if diff_y > 0 else -1
            tail_positions.add(tuple(tail))
        print(f"Current head position: {head}")
        print(f"Current tail position: {tail}")
    print(f"{len(tail_positions)}")


if __name__ == "__main__":
    input_data = read_input()
    list_of_moves = prepare_data(input_data)
    perform_moves_part1(list_of_moves)
