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
        sensors.append(tuple(map(int, re.findall("-?\d+\.?\d*", str_coord[0]))))
        beacons.append(tuple(map(int, re.findall("-?\d+\.?\d*", str_coord[1]))))
    return sensors, beacons


def calculate_distance(sensor, beacon) -> int:
    return abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])


def calculate_intervals(
    distance: list[int], sensors: list[tuple[int, ...]], y: int
) -> list:
    intervals = []
    for i, sensor in enumerate(sensors):
        diff_x = distance[i] - abs(sensor[1] - y)
        if diff_x > 0:
            intervals.append((sensor[0] - diff_x, sensor[0] + diff_x))
    return intervals


def get_all_beacons_on_the_line(beacons: list[tuple[int, ...]], y: int) -> set[int]:
    beacons_on_line = set()
    for beacon in beacons:
        if beacon[1] == y:
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


def find_beacon(distance: list[int], sensors: list[tuple[int, ...]]):
    start_y = 0
    end_y = 4000000
    beacon_y = 0
    beacon_x = 0
    for y in range(start_y, end_y + 1):
        intervals = sorted(calculate_intervals(distance, sensors, y))
        new_interval = list(intervals[0])
        for index in range(1, len(intervals)):
            if (
                intervals[index][0] > new_interval[1]
                and intervals[index][0] - new_interval[1] - 1 == 1
            ):
                beacon_x = new_interval[1] + 1
                beacon_y = y
                break
            if intervals[index][0] < new_interval[0]:
                new_interval[0] = intervals[index][0]
            if intervals[index][1] > new_interval[1]:
                new_interval[1] = intervals[index][1]

        if beacon_x != 0 and beacon_y != 0:
            break

    print(f"Beacon position: {beacon_x}, {beacon_y}")
    frequency = beacon_x * 4000000 + beacon_y
    print(f"Tuning frequency: {frequency}")


if __name__ == "__main__":
    input_data = read_input()
    sensors, beacons = read_sensors_beacons(input_data)
    distance = []
    for index in range(len(sensors)):
        distance.append(calculate_distance(sensors[index], beacons[index]))
    intervals = calculate_intervals(distance, sensors, Y_LINE)
    beacons_x = get_all_beacons_on_the_line(beacons, Y_LINE)
    calculate_positions(intervals, beacons_x)
    find_beacon(distance, sensors)
