from typing import Callable

with open("2015/day08/input.txt") as file:
    data = file.read().splitlines()

def get_raw_string_len(string:str) -> int:
    return len(r"{}".format(string))

def get_string_len(string:str) -> int:
    return len(eval(string))

def get_new_string_len(string:str) -> int:
    return get_raw_string_len(string) + r"{}".format(string).count('"') + 2 + r"{}".format(string).count('\\')

def day08(fn1:Callable, fn2:Callable) -> int:
    total = 0
    for line in data:
        total += fn1(line) - fn2(line)
    return total

def part1() -> int:
    return day08(fn1 = get_raw_string_len, fn2 = get_string_len)

def part2() -> int:
    return day08(fn1 = get_new_string_len, fn2 = get_raw_string_len)

print("Part 1:", part1())
print("Part 2:", part2())
