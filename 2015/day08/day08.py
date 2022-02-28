with open("2015/day08/input.txt") as file:
    data = file.read().splitlines()

def get_raw_string_len(string:str) -> int:
    return len(r"{}".format(string))

def get_string_len(string: str) -> int:
    return len(eval(string))

def get_new_string_len(string:str) -> int:
    return len(r"{}".format(string)) + r"{}".format(string).count('"') + 2 + r"{}".format(string).count('\\')

def part1() -> int:
    total = 0
    for line in data:
        total += get_raw_string_len(line) - get_string_len(line)
    return total

def part2() -> int:
    total = 0
    for line in data:
        total += get_new_string_len(line) - get_raw_string_len(line)
    return total

print("Part 1:", part1())
print("Part 2:", part2())
