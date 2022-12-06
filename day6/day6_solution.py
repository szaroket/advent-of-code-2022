# Advent of code 2022
# Day 6: Tuning Trouble
# https://adventofcode.com/2022/day/6
MIN_LENGTH = 4


def read_input() -> str:
    with open("input.txt", "r") as f:
        data = f.read()
    return data


def prepare_data(data: str) -> list:
    return [sign for sign in data]


def check_marker_index(data: list) -> int:
    start_point = 0
    for index in range(4, len(data)):
        if len(set(data[start_point:index])) == MIN_LENGTH:
            return index
        start_point += 1


if __name__ == "__main__":
    input_data = read_input()
    prepared_data = prepare_data(input_data)
    marker = check_marker_index(prepared_data)
    print(f"The first start-of-packet marker is detected on position: {marker}")
