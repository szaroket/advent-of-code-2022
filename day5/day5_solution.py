# Advent of code 2022
# Day 5: Supply Stacks
# https://adventofcode.com/2022/day/5

from typing import Any
import numpy as np


def read_input() -> str:
    with open("input.txt", "r") as f:
        data = f.read()
    return data


def prepare_data(data: str) -> tuple[dict[Any, list[Any]], list]:
    stacks_of_crates, rearrangement_procedures = data.split("\n\n")
    # prepare list of operations
    operations_list = [
        number
        for number in rearrangement_procedures.replace("\n", " ").split(" ")
        if number.isnumeric()
    ]
    length_of_list = len(operations_list)
    number_of_split = length_of_list / 3
    operations = np.array_split(operations_list, number_of_split)
    # prepare stacks
    stacks_transposed = list(zip(*stacks_of_crates.splitlines()))
    stacks = {}
    for line in stacks_transposed:
        stack = [d for d in line if d.isnumeric() or d.isalpha()]
        if stack:
            key = stack.pop()
            stack.reverse()
            stacks[key] = stack
    return stacks, operations


def get_last_stack(stacks: dict[Any, list[Any]]) -> str:
    combination = []
    for stack in stacks.values():
        combination.append(stack.pop())
    return "".join(combination)


def find_final_combination(stacks: dict[Any, list[Any]], operations: list) -> None:
    for amount, stack_from, stack_to in operations:
        for _ in range(int(amount)):
            stacks[stack_to].append(stacks[stack_from].pop())
    final_combination = get_last_stack(stacks)
    print(f"The final combination is: {final_combination}")


if __name__ == "__main__":
    input_data = read_input()
    stacks, operations = prepare_data(input_data)
    find_final_combination(stacks, operations)
