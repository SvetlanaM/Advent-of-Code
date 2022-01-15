import math
from pyclbr import Function 

with open("2021/day24/input.txt") as file:
    data = file.read().splitlines()

def inp(a:int) -> int:
    return a

def add(a: int, b: int) -> int:
    a += b
    return a 

def mul(a: int, b: int) -> int:
    a *= b
    return a

def div(a: int, b: int) -> int:
    a /= b
    return math.floor(a)

def mod(a:int , b: int) -> int:
    a = a % b
    return a

def eql(a:int, b:int) -> int:
    if a == b:
        a = 1
    else:
        a = 0
    return a

def make_calculations(calc_name: str, a: int, b: int) -> Function:
    if calc_name == 'inp':
        return inp(a)
    if calc_name == 'mul':
        return mul(a, b)
    if calc_name == 'add':
        return add(a, b)
    if calc_name == 'mod':
        return mod(a, b)
    if calc_name == 'div':
        return div(a, b)
    if calc_name == 'eql':
        return eql(a, b)



def remove_duplicates(my_dict: dict[str : str], is_final:bool = False):
    new_dict = {}
    new_arr = []
    
    for i, _ in enumerate(my_dict):
        if not is_final:
            new_dict[list(my_dict[i].keys())[0] % 26] = (list(my_dict[i].values())[0], list(my_dict[i].keys())[0])
        else:
            new_dict[list(my_dict[i].keys())[0]] = (list(my_dict[i].values())[0], list(my_dict[i].keys())[0])
    
    newlist = sorted(new_dict.values(), key=lambda d: "".join(str(d[0])))
    
    for value in newlist:
        temp_dict = {}
        temp_dict[value[1]] = value[0]
        new_arr.append(temp_dict)
    return new_arr


result = [{0:[]}]
temp_result1 = []


def generate_output(data: list[str], result: list(dict[int : list(int)]), skip_modulo: bool):
    result = result
    temp_result = []
    
    for z in result:
        history = [list(z.values())[0]][0]
        z = [list(z.keys())[0]][0]
        for i in range(1, 10):
            x, y, w = 0, 0, 0
            z = z
            temp_dict = {}
            w = i
            var_dict = {'x' : x, 'y' : y, 'z' : z, 'w' : w}
            for j, line in enumerate(data):
                instruction = line.split(" ")
                if instruction[0] == 'inp':
                    continue
                temp = var_dict[instruction[1]]
                if instruction[2] in ['x', 'y', 'z', 'w']:
                    temp2 = var_dict[instruction[2]]
                else:
                    temp2 = instruction[2]
                temp = make_calculations(instruction[0], int(temp), int(temp2))
                var_dict[instruction[1]] = temp    
                if j == 17:
                    temp_dict[temp] = history + [i]
                    temp_result.append(temp_dict)

            print(var_dict)
        # without_duplicates = remove_duplicates(temp_result, len(history) == 13 or skip_modulo)
        without_duplicates = remove_duplicates(temp_result, True)
        result = without_duplicates
           
    # print("result", result)
    print(len(result))
    return result



new_data = [data[x:x+18] for x in range(0, len(data), 18)]

for i, j in enumerate(new_data):
    skip_modulo = False
    
    if i < 1:
        if 'div z 26' in new_data[i+1]:
            skip_modulo = True

    result = generate_output(j, result, skip_modulo)

newlist = min(result, key=lambda d: list(d.keys()))
print(newlist)