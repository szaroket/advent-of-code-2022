# Advent of code 2022
# Day 10: Cathode-Ray Tube
# https://adventofcode.com/2022/day/10
NOOP_CYCLE = 1
ADD_CYCLE = 2

CYCLES = {20: 0, 60: 0, 100: 0, 140: 0, 180: 0, 220: 0}


def read_input() -> str:
    with open("input.txt", "r") as f:
        data = f.read()
    return data


def prepare_data(data: str) -> list:
    return [cmd for cmd in data.split("\n")]


def check_if_correct_cycle(cycle, value_x):
    if cycle in CYCLES.keys():
        print(f"cycle: {cycle} and x {value_x}")
        CYCLES[cycle] = cycle * value_x


def execute_cmd(cmd_list: list):
    cycle = 0
    value_x = 1
    for cmd in cmd_list:
        if cmd == "noop":
            cycle += 1
            check_if_correct_cycle(cycle, value_x)
        else:
            cycle += 1
            check_if_correct_cycle(cycle, value_x)
            cycle += 1
            check_if_correct_cycle(cycle, value_x)
            value_y = int(cmd.split(" ")[1])
            value_x += value_y
    print(sum(CYCLES.values()))


if __name__ == "__main__":
    input_data = read_input()
    cmd_list = prepare_data(input_data)
    execute_cmd(cmd_list)
