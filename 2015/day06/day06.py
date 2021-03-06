import re
import itertools
from collections import Counter 

with open("2015/day06/input.txt") as file:
    data = file.read().splitlines()

def generate_new_set(min_x:int, max_x:int, min_y:int, max_y:int):
    return set(itertools.product(range(int(min_x), int(max_x)+1), range(int(min_y), int(max_y)+1)))

def generate_new_list(min_x:int, max_x:int, min_y:int, max_y:int):
    return list(itertools.product(range(int(min_x), int(max_x)+1), range(int(min_y), int(max_y)+1)))

pattern_for_instructions = '^(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)'


def part1() -> int:
    result_set = set(itertools.product(range(0, 0), repeat=2))

    for line in data:
        result = re.match(pattern_for_instructions, line)
        grouped_data = list(result.groups())
        state, min_x, max_x, min_y, max_y = grouped_data
        if state == 'turn on':
            result_set = set.union(result_set, generate_new_set(min_x, min_y, max_x, max_y))
        elif state == 'turn off':
            result_set = result_set - generate_new_set(min_x, min_y, max_x, max_y)
        elif state == 'toggle':
            temp_set = generate_new_set(min_x, min_y, max_x, max_y)
            diff_set = temp_set.difference(result_set)
            intersection_set = result_set.intersection(temp_set)
            result_set = set.union(diff_set, result_set)
            result_set = result_set - intersection_set

    return len(result_set)

def part2() -> int:
    result_list = []

    for line in data:
        result = re.match(pattern_for_instructions, line)
        grouped_data = list(result.groups())
        state, min_x, max_x, min_y, max_y = grouped_data
        if state == 'turn on':
            result_list += generate_new_list(min_x, min_y, max_x, max_y)
        elif state == 'turn off':
            list_difference = Counter(result_list) - Counter(generate_new_list(min_x, min_y, max_x, max_y))
            result_list = list(list_difference.elements())
        elif state == 'toggle':
            for _ in range(0, 2):
                result_list += generate_new_list(min_x, min_y, max_x, max_y)

    return len(result_list)
    


print("Part 1:", part1())
print("Part 2:", part2())



