# Advent of code 2022
# Day 3: Rucksack Reorganization
# https://adventofcode.com/2022/day/3

import numpy as np


def read_input() -> str:
    with open("input.txt", "r") as f:
        data = f.read()
    return data


def prepare_data(data: str) -> list:
    return [list(items) for items in data.split("\n")]


def check_common_items(items: list) -> list:
    compartments = np.array_split(items, 2)
    common_items = np.intersect1d(compartments[0], compartments[1])
    # print(f"Common items between two compartments are: {common_items}")
    return common_items


def calculate_items_priority(items_list: list[list]) -> int:
    total_sum = 0
    for items in items_list:
        common_items = check_common_items(items)
        priorities_sum = 0
        for item in common_items:
            if item.islower():
                priorities_sum = priorities_sum + (ord(item) - ord("a") + 1)
            else:
                priorities_sum = priorities_sum + (ord(item) - ord("A") + 27)
        # print(f"The priority of {item} is: {priorities_sum}")
        total_sum = total_sum + priorities_sum
    print(f"The sum of the priorities of items is: {total_sum}")


if __name__ == "__main__":
    input_data = read_input()
    prepared_data = prepare_data(input_data)
    calculate_items_priority(prepared_data)
