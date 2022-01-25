
import re 
from functools import reduce

with open("2015/day02/input.txt") as file:
    data:list[str]= file.read().splitlines()


def find_numbers(square: list[str]) -> list[int]:
    numbers = re.findall('\d+', square)
    return [int(number) for number in numbers]

def make_calculation(square: list[int]) -> int:
    l, w, h = find_numbers(square)
    a = [l*w, w*h, l*h]
    return (2 * a[0]) + (2 * a[1]) + (2 * a[2]) + min(a)

def smallest_calculation(square: list[int]) -> int:
    l, w, h = find_numbers(square)
    temp_arr = sorted([l, w, h])
    return (temp_arr[0]*2 + temp_arr[1]*2) + (l*w*h)


def part1() -> int: 
    total = reduce(lambda x, y: x+y, list(map(make_calculation, data)))
    return total

def part2() -> int:
    total = reduce(lambda x, y: x+y, list(map(smallest_calculation, data)))
    return total

print("Total:", part1())
print("Min:", part2())

