# Advent of code 2022
# Day 10: Cathode-Ray Tube
# https://adventofcode.com/2022/day/10
from typing import Tuple

import numpy as np

CYCLES = {20: 0, 60: 0, 100: 0, 140: 0, 180: 0, 220: 0}
LIT_PIXEL = "#"
GRID = [[" "] * 40 for _ in range(6)]


def read_input() -> str:
    with open("input.txt", "r") as f:
        data = f.read()
    return data


def prepare_data(data: str) -> list:
    return [cmd for cmd in data.split("\n")]


def draw_symbol(cycle: int, x: int, row: int) -> None:
    if abs(x - (cycle % 40)) <= 1:
        GRID[row][cycle % 40] = LIT_PIXEL


def check_if_correct_cycle(cycle: int, value_x: int) -> None:
    if cycle in CYCLES.keys():
        CYCLES[cycle] = cycle * value_x


def perform_procedure(cycle: int, value_x: int, row: int) -> tuple[int, int]:
    draw_symbol(cycle, value_x, row)
    cycle += 1
    if cycle % 40 == 0:
        row += 1
    check_if_correct_cycle(cycle, value_x)
    return cycle, row


def execute_cmd(cmd_list: list) -> None:
    cycle = 0
    value_x = 1
    row = 0
    for cmd in cmd_list:
        cycle, row = perform_procedure(cycle, value_x, row)
        if cmd != "noop":
            cycle, row = perform_procedure(cycle, value_x, row)
            value_y = int(cmd.split(" ")[1])
            value_x += value_y
    sum_cycle = sum(CYCLES.values())
    print(f"The sum of these six signal strengths: {sum_cycle}")
    np.set_printoptions(linewidth=np.inf)
    print(np.array(GRID))


if __name__ == "__main__":
    input_data = read_input()
    cmd_list = prepare_data(input_data)
    execute_cmd(cmd_list)
