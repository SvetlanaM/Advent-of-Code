from itertools import product
import numpy as np

with open("2021/day15/input.txt", encoding='utf-8') as file:
    data = file.read().splitlines()

data = [int(line) for line in data]
input_array = [list(map(int,str(line))) for line in data]
stack = []
result = 0
start_position = (0, 0)
stack.append(start_position)

input_array_copy = [ [float('inf')]*len(input_array) for i in range(len(input_array))]

input_array_copy[0][0] = 0

original_length = len(input_array_copy)
input_array_new = input_array


while stack:
    cur_position = stack.pop(0)
    x, y = cur_position

    # if input_array[x][y] == None:
    #     continue

    left = y-1
    right = y+1
    up = x-1
    down = x+1

    temp_arr = [(x, left), (x, right), (up, y), (down, y)]


    filtered_coords = list(filter(lambda coord: (coord[0] >= 0 and coord[0] < len(input_array)) and \
                                                (coord[1] >= 0 and coord[1] < len(input_array)) and \
                                                input_array[coord[0]][coord[1]] != None, temp_arr))
    
    sorted_coords = [x for _,x in sorted(zip(map(lambda x: input_array[x[0]][x[1]], filtered_coords), filtered_coords))]

  
    for pair in sorted_coords:
        if (input_array[pair[0]][pair[1]] + input_array_copy[x][y] < input_array_copy[pair[0]][pair[1]]):
            input_array_copy[pair[0]][pair[1]] = input_array[pair[0]][pair[1]] + input_array_copy[x][y]
    
            stack.append(pair)
    
    input_array[x][y] = None


        
print(input_array_copy[len(input_array_copy)-1][len(input_array_copy)-1])