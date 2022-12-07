# Advent of code 2022
# Day 7: No Space Left On Device
# https://adventofcode.com/2022/day/7
SIZE_MIN = 100000
TOTAL_DISK_SPACE = 70000000
NEEDED_SPACE = 30000000
FOLDERS_SIZES = []


def read_input() -> str:
    with open("input.txt", "r") as f:
        data = f.read()
    return data


def prepare_data(data: str) -> list:
    return [cmd for cmd in data.split("\n")]


def create_folder_structure(cmd_list: list) -> dict:
    main_folder = {"children": {}, "parent": "MAIN_FOLDER"}
    current_folder = main_folder
    for cmd in cmd_list:
        cmd = cmd.split(" ")
        if cmd[0] == "$":
            if cmd[1] == "cd":
                if cmd[2] == "/":
                    current_folder = main_folder
                elif cmd[2] == "..":
                    current_folder = current_folder["parent"]
                else:
                    current_folder["children"][cmd[2]] = {
                        "children": {},
                        "parent": current_folder,
                    }
                    current_folder = current_folder["children"][cmd[2]]
        elif cmd[0] != "dir":
            current_folder["children"][cmd[1]] = {
                "parent": current_folder,
                "file_size": cmd[0],
            }
    return main_folder


def calculate_sizes(folders: dir) -> int:
    if "file_size" in folders:
        return int(folders["file_size"])

    total_size = 0
    for folder in folders["children"].values():
        folder_size = calculate_sizes(folder)
        if folder_size is not None:
            total_size += folder_size
    FOLDERS_SIZES.append(total_size)
    return total_size


def get_result_part1() -> int:
    return sum(number for number in FOLDERS_SIZES if number <= SIZE_MIN)


def get_result_part2() -> int:
    FOLDERS_SIZES.sort()
    last_index = len(FOLDERS_SIZES) - 1
    size_of_unused_space = TOTAL_DISK_SPACE - FOLDERS_SIZES[last_index]
    space_to_free = NEEDED_SPACE - size_of_unused_space
    for size in FOLDERS_SIZES:
        if size >= space_to_free:
            return size


if __name__ == "__main__":
    input_data = read_input()
    list_of_cmd = prepare_data(input_data)
    folder_structure = create_folder_structure(list_of_cmd)
    total = calculate_sizes(folder_structure)
    result1 = get_result_part1()
    print(f"The sum of the total sizes of directories is: {result1}")
    result2 = get_result_part2()
    print(f"Size of folder to delete: {result2}")
