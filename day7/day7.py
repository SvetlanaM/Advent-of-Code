import functools
from typing import Callable

test_data = [16,1,2,0,4,2,7,1,2,14]

with open("day7/day7.txt", encoding='utf-8') as file:
    data = file.read().splitlines()[0].split(",")
data = [int(line) for line in data]

def get_sorted_data(input_data: list[int]) -> list[int]:
    sortedArray = sorted(input_data)
    return sortedArray

sorted_array = get_sorted_data(data)
count = len(sorted_array) - 1

def median() -> float:
    if count % 2 != 0:
        return float(sorted_array[int(count/2)])
    else:
        return float(sorted_array[int(count / 2)] + sorted_array[int(count / 2 - 1)] / 2)

def average() -> float:
    return sum(sorted_array) / count

def sum_of_fuel(positions: list[int], target: int) -> int:
    sum = 0
    for i in positions:
        temp = abs(i - target)
        sum += temp
    return sum

def sum_fuel_dynamic(positions: list[int], target: int) -> int:
    sum = 0
    for i in positions:
        temp = abs(i - target) * (abs(target - i) + 1) / 2
        sum += temp
    return int(sum)

def traverse_for_min(positions: list[int], initial_position: int, compute_fuel: Callable[[int], int]) -> int:
    
    min_fuel = compute_fuel(positions, initial_position)
    current_position = initial_position + 1
    current_fuel = min_fuel
    
    while True:
        current_fuel = compute_fuel(positions, current_position)
        if current_fuel < min_fuel:
            min_fuel = current_fuel
        current_position += 1
        if (current_fuel < min_fuel or current_position <= max(sorted_array)):
            break
        
    return min_fuel

estimate_first:int = int(median())
estimate_second = int(average())
result_first:int = traverse_for_min(positions=sorted_array, initial_position=estimate_first, compute_fuel=sum_of_fuel)
result_second:int = traverse_for_min(positions=sorted_array, initial_position=estimate_second, compute_fuel=sum_fuel_dynamic)
print(result_first)
print(result_second)