import re 
with open("2021/day24/input.txt") as file:
    data = file.read().splitlines()

pattern_array = []
divided_data = [data[x:x+18] for x in range(0, len(data), 18)]


def find_z_number(x: int, y: int, z: int, pz: int, w: int) -> list(int):
    temp_arr = []
    i = pz - w - y
    if i % 26 == 0:
        temp_arr.append(i//26 * z)
    if 0 <= w-x < 26:
        temp_z = pz * z
        temp_arr.append(w-x+temp_z)
    return temp_arr

for i, j in enumerate(divided_data[::-1]):
    temp_dict = {}
    for a, b in enumerate(j):
        if a == 4:
            temp_dict['z'] = int(re.findall(r'-?\d+', b)[0])
        if a == 5:
            temp_dict['x'] = int(re.findall(r'-?\d+', b)[0])
        if a == 15:
            temp_dict['y'] = int(re.findall(r'-?\d+', b)[0])
    pattern_array.append(temp_dict)




def find_monad_number(range: range) -> dict[int : list(int)]:
    z_results = {0 : []}
    final_result = {}
    while len(pattern_array) != 0:
        temp_dict = {}
        for z in z_results:
            for w in range:
                new_z_results = find_z_number(
                    pattern_array[0]['x'],
                    pattern_array[0]['y'],
                    pattern_array[0]['z'],
                    z,
                    w
                    )          
                for new_z in new_z_results:
                    temp_dict[new_z] = w
                    
                    if new_z in final_result:
                        final_result[new_z] = [w] + final_result.get(z)
                    else:
                        if final_result.get(z) is not None:
                            final_result[new_z] = [w] + final_result.get(z)
                        else:
                            final_result[new_z] = [w] 
            z_results = temp_dict
        pattern_array.pop(0)
    return final_result

print("Max:", find_monad_number(range(1, 10)))
print("Min:", find_monad_number(range(9, 0, -1)))

