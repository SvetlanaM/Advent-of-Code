from collections import Counter

with open("2015/day01/input.txt") as file:
    data = file.read().splitlines()

def part1():
    array_by_items = []

    for d in data[0]:
        array_by_items.append(d)

    print(Counter(array_by_items)['('] - Counter(array_by_items)[')'])

part1()


def part2():
    temp_dict = {'(' : 0, ')' : 0}
    result = 0

    for i, d in enumerate(data[0]):
        temp_dict[d] += 1
        result = temp_dict['('] - temp_dict[')']
        if result == -1:
            print(i+1)
            return i


part2()