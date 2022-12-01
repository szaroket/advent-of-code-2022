# Advent of code 2022
# Day 1: Calorie Counting
# https://adventofcode.com/2022/day/1

TOP_NUMBER_OF_ELVES = 3


def read_input() -> list:
    with open("input.txt", "r") as f:
        data = f.read()
    return data


def prepare_data(data: list) -> list:
    return [list(map(int, elf.split("\n"))) for elf in data.split("\n\n")]


def get_max_calories(data: list) -> int:
    return sum(max(data, key=sum))


def sum_and_sort_calories(data: list) -> list:
    return sorted([sum(elf) for elf in data], reverse=True)


def sum_top_three_calories(data: list) -> int:
    return sum(data[0:TOP_NUMBER_OF_ELVES])


if __name__ == "__main__":
    input_data = read_input()
    prepared_data = prepare_data(input_data)
    max_calories = get_max_calories(prepared_data)
    print(f"The highest number of calories carried by the Elf: {max_calories}")
    sorted_total_calories = sum_and_sort_calories(prepared_data)
    top_three_sum = sum_top_three_calories(sorted_total_calories)
    print(
        f"The highest number of calories carried by the top three Elves: {top_three_sum}"
    )
