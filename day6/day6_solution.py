# Advent of code 2022
# Day 6: Tuning Trouble
# https://adventofcode.com/2022/day/6
MIN_LENGTH_PART1 = 4
MIN_LENGTH_PART2 = 14


def read_input() -> str:
    with open("input.txt", "r") as f:
        data = f.read()
    return data


def prepare_data(data: str) -> list:
    return [sign for sign in data]


def check_marker_index(data: list, min_length: int) -> int:
    start_point = 0
    for index in range(min_length, len(data)):
        if len(set(data[start_point:index])) == min_length:
            return index
        start_point += 1


if __name__ == "__main__":
    input_data = read_input()
    prepared_data = prepare_data(input_data)
    marker1 = check_marker_index(prepared_data, MIN_LENGTH_PART1)
    print(f"The first start-of-packet marker is detected on position: {marker1}")
    marker2 = check_marker_index(prepared_data, MIN_LENGTH_PART2)
    print(f"The first start-of-packet marker is detected on position: {marker2}")
