# Advent of code 2022
# Day 13: Distress Signal
# https://adventofcode.com/2022/day/13


def read_input() -> str:
    with open("input.txt", "r") as f:
        data = f.read()
    return data


def prepare_data(data: str) -> list[list]:
    return [list(map(eval, x.split("\n"))) for x in data.split("\n\n")]


def compare_values(left, right):
    if isinstance(left, int) and isinstance(right, list):
        left = [left]

    if isinstance(left, list) and isinstance(right, int):
        right = [right]

    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1
        elif left == right:
            return 0
        else:
            return -1

    if isinstance(left, list) and isinstance(right, list):
        index = 0
        while index < len(left) and index < len(right):
            in_order = compare_values(left[index], right[index])
            if in_order == 1:
                return 1
            if in_order == -1:
                return -1
            index += 1

        if index == len(left):
            if len(left) == len(right):
                return 0
            return 1

        if index == len(right):
            return -1


def get_solution_part1(data: list[list]):
    solution = 0
    for i, pair in enumerate(data):
        left, right = pair
        if compare_values(left, right) == 1:
            solution += i + 1
    print(f"The sum of the indices of pairs: {solution}")


if __name__ == "__main__":
    input_data = read_input()
    prepared_data = prepare_data(input_data)
    get_solution_part1(prepared_data)
