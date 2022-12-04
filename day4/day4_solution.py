# Advent of code 2022
# Day 4: Camp Cleanup
# https://adventofcode.com/2022/day/4


def read_input() -> str:
    with open("input.txt", "r") as f:
        data = f.read()
    return data


def prepare_data(data: str) -> list[list]:
    return [
        [int(coordinate) for coordinate in coordinates.replace("-", ",").split(",")]
        for coordinates in data.split("\n")
    ]


def calculate_overlapping(coordinates_list: list[list]) -> None:
    overlapping_sum = 0
    for a, b, x, y in coordinates_list:
        if (a <= x and b >= y) or (a >= x and b <= y):
            overlapping_sum += 1
    print(f"Number of pairs that one range fully contain the other: {overlapping_sum}")


if __name__ == "__main__":
    input_data = read_input()
    prepared_data = prepare_data(input_data)
    calculate_overlapping(prepared_data)
