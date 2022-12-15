# Advent of code 2022
# Day 15: Beacon Exclusion Zone
# https://adventofcode.com/2022/day/15
import re

Y_LINE = 2000000


def read_input() -> list[str]:
    with open("input.txt", "r") as f:
        data = f.read().split("\n")
    return data


def read_sensors_beacons(
    lines: list[str],
) -> tuple[list[tuple[int, ...]], list[tuple[int, ...]]]:
    sensors = []
    beacons = []
    for line in lines:
        str_coord = line.split(": ")
        sensors.append(tuple(map(int, re.findall(r"\d+", str_coord[0]))))
        beacons.append(tuple(map(int, re.findall(r"\d+", str_coord[1]))))
    return sensors, beacons


def calculate_distance(sensor, beacon) -> int:
    return abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])


def calculate_intervals(distance: list[int], sensors: list[tuple[int, ...]]) -> list:
    intervals = []
    for i, sensor in enumerate(sensors):
        diff_x = distance[i] - abs(sensor[1] - Y_LINE)
        if diff_x > 0:
            intervals.append((sensor[0] - diff_x, sensor[0] + diff_x))
    return intervals


def get_all_beacons_on_the_line(beacons: list[tuple[int, ...]]) -> set[int]:
    beacons_on_line = set()
    for beacon in beacons:
        if beacon[1] == Y_LINE:
            beacons_on_line.add(beacon[0])
    return beacons_on_line


def calculate_positions(intervals: list, beacons_x: set[int]):
    min_x = min(x[0] for x in intervals)
    max_x = max(x[1] for x in intervals)
    positions = 0
    for x in range(min_x, max_x + 1):
        if x not in beacons_x:
            for left, right in intervals:
                if left <= x <= right:
                    positions += 1
                    break
    print(f"Positions which cannot contain a beacon: {positions}")


if __name__ == "__main__":
    input_data = read_input()
    sensors, beacons = read_sensors_beacons(input_data)
    distance = []
    for index in range(len(sensors)):
        distance.append(calculate_distance(sensors[index], beacons[index]))
    intervals = calculate_intervals(distance, sensors)
    beacons_x = get_all_beacons_on_the_line(beacons)
    calculate_positions(intervals, beacons_x)
