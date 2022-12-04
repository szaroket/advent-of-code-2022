# Advent of code 2022
# Day 3: Rucksack Reorganization
# https://adventofcode.com/2022/day/3

import numpy as np


def read_input() -> str:
    with open("input.txt", "r") as f:
        data = f.read()
    return data


def prepare_data_part1(data: str) -> list:
    return [list(items) for items in data.split("\n")]


def prepare_data_part2(data: list) -> list:
    length_of_list = len(data)
    number_of_split = length_of_list / 3
    return np.array_split(data, number_of_split)


def check_common_items_part1(items: list) -> list:
    compartments = np.array_split(items, 2)
    common_items = np.intersect1d(compartments[0], compartments[1])
    return list(common_items)


def check_common_items_part2(items: tuple) -> list:
    return list(set(items[0]) & set(items[1]) & set(items[2]))


def calculate_items_priority(common_items: list) -> int:
    priorities_sum = 0
    for item in common_items:
        if item.islower():
            priorities_sum = priorities_sum + (ord(item) - ord("a") + 1)
        else:
            priorities_sum = priorities_sum + (ord(item) - ord("A") + 27)
    return priorities_sum


def get_solution_part1(items_list: list) -> None:
    total_sum = 0
    for items in items_list:
        common_items = check_common_items_part1(items)
        priorities_sum = calculate_items_priority(common_items)
        total_sum = total_sum + priorities_sum
    print(f"PART 1: The sum of the priorities of items is: {total_sum}")


def get_solution_part2(items_list: list[tuple]) -> None:
    total_sum = 0
    for items in items_list:
        common_items = check_common_items_part2(items)
        priorities_sum = calculate_items_priority(common_items)
        total_sum = total_sum + priorities_sum
    print(f"PART 2: The sum of the priorities of items is: {total_sum}")


if __name__ == "__main__":
    input_data = read_input()
    prepared_data_part1 = prepare_data_part1(input_data)
    get_solution_part1(prepared_data_part1)
    data_for_part2 = prepare_data_part2(prepared_data_part1)
    get_solution_part2(data_for_part2)
