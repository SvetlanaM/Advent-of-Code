from functools import reduce
import re
from typing import final

with open("2021/day13/input.txt", encoding='utf-8') as file:
    data = file.read().split("\n")

index_of_divider = data.index("")
arr_of_numbers = data[0:index_of_divider]
arr_of_directions = data[index_of_divider+1: len(data)]


def get_max_number(key):
    max = 0
    for i in arr_of_numbers:
        i = int(i.split(",")[key])
        if i > max:
            max = i
    
    return max

max_x = get_max_number(0)
max_y = get_max_number(1)
grid = [[' ' for i in range(max_x+1)] for j in range(max_y+1)]

def create_grid():
    for key, line in enumerate(arr_of_numbers):
        grid[int(line.split(",")[1])][int(line.split(",")[0])] = "█"
        pass
    
    return grid
        
create_grid()

def get_direction(line):
    if 'x' in arr_of_directions[line]: return 'x'
    else:
        return 'y'



def get_folding(line):
    temp = re.findall(r'\b\d+\b', arr_of_directions[line])
    fold_by_y = int(temp[0])
    return fold_by_y

def folded_number(arr):
    if len(arr) % 2 == 0:
        return 0
    else:
        return 1

def create_folded_grid(grid_down, grid_up, fold_by):
    for key, row in enumerate(grid_down):
        for col_key, col in enumerate(row):
            if col == "█":
                temp = abs(key-fold_by+1)
                grid_up[temp][col_key] = "█"
    return grid_up


def folding():
    final_grid = create_grid()
    for key, i in enumerate(arr_of_directions):
        direction = get_direction(key)
        fold_by_y = get_folding(key)

        if key == 0:
            if direction == 'x':
                final_grid = [list(i) for i in zip(*final_grid)]
        else:
            last_direction = get_direction(key-1)
            if last_direction != direction:
                if last_direction == 'y':
                    final_grid = [list(i) for i in zip(*final_grid)]
                elif last_direction == 'x':
                    for _ in range(0,3):
                        final_grid = [list(i) for i in zip(*final_grid)]
                        
        folded_grid_up = final_grid[:][0:fold_by_y]
        folded_grid_down = final_grid[:][fold_by_y+1:len(final_grid)]
        final_grid = create_folded_grid(folded_grid_down, folded_grid_up, fold_by_y)

    print("--")
    for line in final_grid:
        print("".join(line))
    return final_grid
    

#part1
# flatten_map = reduce(list.__add__, folded_grid_up)
# result = list(filter(lambda x: x == "#", flatten_map))

# flatten_map1 = reduce(list.__add__, folded_grid_left)
# result1 = list(filter(lambda x: x == "#", flatten_map1))


folding()




