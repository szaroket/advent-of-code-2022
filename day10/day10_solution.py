# Advent of code 2022
# Day 10: Cathode-Ray Tube
# https://adventofcode.com/2022/day/10
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


def draw_symbol(cycle, x, row):
    if abs(x - (cycle % 40)) <= 1:
        GRID[row][cycle % 40] = LIT_PIXEL


def check_if_correct_cycle(cycle, value_x):
    if cycle in CYCLES.keys():
        print(f"cycle: {cycle} and x {value_x}")
        CYCLES[cycle] = cycle * value_x


def execute_cmd(cmd_list: list):
    cycle = 0
    value_x = 1
    row = 0
    for cmd in cmd_list:
        if cmd == "noop":
            draw_symbol(cycle, value_x, row)
            cycle += 1
            check_if_correct_cycle(cycle, value_x)
            if cycle % 40 == 0:
                row += 1
        else:
            draw_symbol(cycle, value_x, row)
            cycle += 1
            if cycle % 40 == 0:
                row += 1
            check_if_correct_cycle(cycle, value_x)
            draw_symbol(cycle, value_x, row)
            cycle += 1
            if cycle % 40 == 0:
                row += 1
            check_if_correct_cycle(cycle, value_x)
            value_y = int(cmd.split(" ")[1])
            value_x += value_y
    print(sum(CYCLES.values()))
    np.set_printoptions(linewidth=np.inf)
    print(np.array(GRID))


if __name__ == "__main__":
    input_data = read_input()
    cmd_list = prepare_data(input_data)
    execute_cmd(cmd_list)
