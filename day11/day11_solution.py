# Advent of code 2022
# Day 11: Monkey in the Middle
# https://adventofcode.com/2022/day/11
import re


def read_input() -> str:
    with open("input.txt", "r") as f:
        data = f.read()
    return data


def prepare_data(data: str) -> list:
    return [
        instructions.replace("  ", "").split("\n")
        for instructions in data.split("\n\n")
    ]


def create_monkey_instruction_struct(instructions_list: list) -> list[dict]:
    monkeys_array = []
    for instructions in instructions_list:
        monkey_items = re.findall(r"\d+", instructions[1])
        monkey_operation = re.findall(r"\*|\+", instructions[2])
        monkey_number_operation = re.findall(r"\d+", instructions[2])
        monkey_test = re.findall(r"\d+", instructions[3])
        monkey_if_true = re.findall(r"\d+", instructions[4])
        monkey_if_false = re.findall(r"\d+", instructions[5])
        monkeys_array.append(
            {
                "items": [int(x) for x in monkey_items],
                "operation": monkey_operation[0],
                "number": int(monkey_number_operation[0])
                if monkey_number_operation
                else -1,
                "test": int(monkey_test[0]),
                "if_true": int(monkey_if_true[0]),
                "if_false": int(monkey_if_false[0]),
                "inspected_number": 0,
            }
        )
    return monkeys_array


def execute_rounds(monkeys: list[dict], rounds: int):
    for _ in range(rounds):
        for monkey in monkeys:
            items_index = 0
            for item in monkey["items"]:
                # print(f"Monkey inspects an item with a worry level of {item}")
                if monkey["operation"] == "*":
                    if monkey["number"] == -1:
                        worry_level = item * item
                    else:
                        worry_level = item * monkey["number"]
                if monkey["operation"] == "+":
                    if monkey["number"] == -1:
                        worry_level = item + item
                    else:
                        worry_level = item + monkey["number"]
                # print(f"  Worry level is multiplied by {monkey['operation']} to {worry_level}")
                divided_worry_level = worry_level // 3
                if divided_worry_level % monkey["test"] == 0:
                    # print(f"  Item with worry level {divided_worry_level} is thrown to monkey {monkey['if_true']}")
                    monkeys[monkey["if_true"]]["items"].append(divided_worry_level)
                else:
                    # print(f"  Current worry level is not divisible by {monkey['test']}")
                    # print(f"  Item with worry level {divided_worry_level} is thrown to monkey {monkey['if_false']}")
                    monkeys[monkey["if_false"]]["items"].append(divided_worry_level)
                items_index += 1
                monkey["inspected_number"] += 1
            monkey["items"] = monkey["items"][items_index:]
    inspected_list = sorted(
        [monkey["inspected_number"] for monkey in monkeys], reverse=True
    )
    print(
        f"The level of monkey business after 20 rounds of stuff-slinging simian shenanigans: {inspected_list[0] * inspected_list[1]}"
    )


if __name__ == "__main__":
    input_data = read_input()
    prepared_data = prepare_data(input_data)
    monkeys_arr = create_monkey_instruction_struct(prepared_data)
    execute_rounds(monkeys_arr, 20)
