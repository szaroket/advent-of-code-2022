# Advent of code 2022
# Day 1: Calorie Counting
# https://adventofcode.com/2022/day/1


def read_input() -> list:
    with open("input.txt", "r") as f:
        data = f.read()
    return data


def prepare_data(data: list) -> list:
    return [list(map(int, elf.split("\n"))) for elf in data.split("\n\n")]


def get_max_calories(data: list) -> list:
    return sum(max(data, key=sum))


if __name__ == "__main__":
    input_data = read_input()
    prepared_data = prepare_data(input_data)
    max_calories = get_max_calories(prepared_data)
    print(f"The highest number of calories carried by an elf: {max_calories}")
