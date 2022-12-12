# Advent of code 2022
# Day 12: Hill Climbing Algorithm
# https://adventofcode.com/2022/day/12
import string
from collections import deque as queue
import numpy as np


START_POINT = "S"
END_POINT = "E"


def read_input() -> str:
    with open("input.txt", "r") as f:
        data = f.read()
    return data


def prepare_data(data: str) -> list[list]:
    return [list(row) for row in data.split("\n")]


def find_point(graph: list[list], point: str) -> tuple:
    for row in range(len(graph)):
        for col in range(len(graph[0])):
            if graph[row][col] == point:
                return col, row


def solution_part1(
    graph: list[list[string]], starting_point: tuple, ending_point: tuple
):
    direction_x = [-1, 0, 1, 0]
    direction_y = [0, 1, 0, -1]
    visited_array = [[False for i in range(len(graph[0]))] for i in range(len(graph))]
    q = queue()
    q.append((0, starting_point))
    graph[starting_point[1]][starting_point[0]] = "a"
    graph[ending_point[1]][ending_point[0]] = "z"
    visited_array[starting_point[1]][starting_point[0]] = True
    while len(q) > 0:
        steps, cell = q.popleft()
        if cell == ending_point:
            return steps
        x, y = cell
        for i in range(4):
            adjx = x + direction_x[i]
            adjy = y + direction_y[i]
            if adjx < 0 or adjy < 0 or adjx >= len(graph[0]) or adjy >= len(graph):
                continue
            if visited_array[adjy][adjx]:
                continue
            if not (ord(graph[adjy][adjx]) <= ord(graph[y][x]) + 1):
                continue
            q.append((steps + 1, (adjx, adjy)))
            visited_array[adjy][adjx] = True


if __name__ == "__main__":
    input_data = read_input()
    prepared_data = prepare_data(input_data)
    starting_point_coordinates = find_point(prepared_data, START_POINT)
    ending_point_coordinated = find_point(prepared_data, END_POINT)
    steps = solution_part1(
        prepared_data, starting_point_coordinates, ending_point_coordinated
    )
    print(
        f"The fewest steps required to move from your current position to the location: {steps}"
    )
