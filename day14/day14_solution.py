# Advent of code 2022
# Day 14: Regolith Reservoir
# https://adventofcode.com/2022/day/14
import copy
from typing import Any, Generator, Tuple

SAND_SOURCE = (500, 0)
FILLED = set()


def read_input() -> str:
    with open("input.txt", "r") as f:
        data = f.read()
    return data


def prepare_data(data: str) -> list:
    return data.strip().split("\n")


def create_rock_coordinates(data: list) -> list[Generator[tuple[int, ...], Any, None]]:
    coord_list = []
    for line in data:
        coord_list.append(
            tuple(map(int, coord.split(","))) for coord in line.strip().split(" -> ")
        )
    return coord_list


def fill_map_with_rocks(coords: list[Generator[tuple[int, ...], Any, None]]) -> None:
    for rocks in coords:
        rocks = list(rocks)
        for i in range(1, len(rocks)):
            current_x, current_y = rocks[i]
            previous_x, previous_y = rocks[i - 1]

            if current_y != previous_y and current_x == previous_x:
                for y in range(
                    min(current_y, previous_y), max(current_y, previous_y) + 1
                ):
                    FILLED.add((current_x, y))

            if current_x != previous_x and current_y == previous_y:
                for x in range(
                    min(current_x, previous_x), max(current_x, previous_x) + 1
                ):
                    FILLED.add((x, current_y))


def get_max_high():
    return max([rock[1] for rock in FILLED])


def simulate_sand(max_high: int) -> bool:
    x, y = SAND_SOURCE
    while y <= max_high:
        if (x, y + 1) not in FILLED:
            y += 1
            continue

        if (x - 1, y + 1) not in FILLED:
            x -= 1
            y += 1
            continue

        if (x + 1, y + 1) not in FILLED:
            x += 1
            y += 1
            continue

        FILLED.add((x, y))
        return True
    return False


def simulate_sand2(max_high: int) -> tuple[int, int]:
    x, y = SAND_SOURCE
    while y <= max_high:
        if (x, y + 1) not in FILLED2:
            y += 1
            continue

        if (x - 1, y + 1) not in FILLED2:
            x -= 1
            y += 1
            continue

        if (x + 1, y + 1) not in FILLED2:
            x += 1
            y += 1
            continue

        break

    FILLED2.add((x, y))
    return x, y


if __name__ == "__main__":
    input_data = read_input()
    prepared_data = prepare_data(input_data)
    rock_coord = create_rock_coordinates(prepared_data)
    fill_map_with_rocks(rock_coord)
    max_high = get_max_high()

    global FILLED2
    FILLED2 = copy.deepcopy(FILLED)

    units = 0
    while True:
        result = simulate_sand(max_high)
        if not result:
            break
        units += 1
    print(f"Number of sand units: {units}")

    units2 = 0
    while True:
        x, y = simulate_sand2(max_high)
        units2 += 1
        if (x, y) == SAND_SOURCE:
            break
    print(f"Number of sand units for part2: {units2}")
