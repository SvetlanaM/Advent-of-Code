from itertools import product
import itertools
with open("2021/day11/input.txt", encoding='utf-8') as file:
    data = file.read().splitlines()
data = [int(line) for line in data]
input_array = [list(map(int,str(line))) for line in data]

number_of_flash = 0
stacked_list = []


def update_number(x, y):
    if input_array[x][y] != 0:
        input_array[x][y] += 1
        
    if input_array[x][y] == 10:
        stacked_list.append((x, y))
   
    
for i in range(0, 100):
    for row in range(len(input_array)):
        for col in range(len(input_array[row])):
            input_array[row][col] += 1
            if input_array[row][col] > 9:
                stacked_list.append((row, col))
                
            while stacked_list:

                number_of_flash += 1
                x, y = stacked_list.pop()
                input_array[x][y] = 0

                for pair in itertools.product([-1, 0, 1], [-1, 0, 1]):
                    if ((x+pair[0] >= 0 and x+pair[0] <= len(input_array)-1) and (y+pair[1] >= 0 and y+pair[1] < len(input_array)-1)):
                        update_number(x+pair[0], y+pair[1])
        
                  
print(number_of_flash)
