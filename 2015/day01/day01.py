from collections import Counter

with open("2015/day01/input.txt") as file:
    data:str = file.read().splitlines()[0]

def part1() -> None:
    array_by_items:list(str) = []

    for d in data:
        array_by_items.append(d)

    print(Counter(array_by_items)['('] - Counter(array_by_items)[')'])

part1()


def part2() -> int:
    result:int = 0
    i:int = 0
    while result != -1:
        result =  result + 1 if data[i] == "(" else result-1
        i += 1
    return i


    #solution with for loop
    # temp_dict = {'(' : 0, ')' : 0}
    # for i, d in enumerate(data):
    #     temp_dict[d] += 1
    #     result = temp_dict['('] - temp_dict[')']
    #     if result == -1:
    #         return i+1

print(part2())