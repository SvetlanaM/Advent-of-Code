with open("2021/day15/input.txt", encoding='utf-8') as file:
    data = file.read().splitlines()

data = [int(line) for line in data]
input_array = [list(map(int,str(line))) for line in data]


input_array_new = input_array
new_arr = input_array.copy()
max_arr_size = len(input_array[0])

for i in range(0,4):
    for x in range(0, len(new_arr)):
        new_arr[x] = new_arr[x] + list(map(lambda x: x+1 if (x+1 < 10) else 1, new_arr[x][-max_arr_size:]))
    

for i in range(0,4):
    for j in new_arr[-max_arr_size:]:
        new_row = list(map(lambda x: x+1 if (x+1 < 10) else 1, j))
        new_arr.append(new_row)


def djikstra(input_array: list(int)) -> None:
    input_array_copy = [ [float('inf')]*len(input_array) for i in range(len(input_array))]
    input_array_copy[0][0] = 0
    stack = []
    start_position = (0, 0)
    stack.append(start_position)

    while stack:

        stack = [x for _,x in sorted(zip(map(lambda x: input_array_copy[x[0]][x[1]], stack), stack))]
        cur_position = stack.pop(0)
        x, y = cur_position

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

djikstra(new_arr)