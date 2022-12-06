import re

INPUT_FILE = '2022/day05/test_input.txt'
pattern_for_instructions = '^move (\d+) from (\d+) to (\d+)'

with open(INPUT_FILE) as file:
    data = file.read().splitlines()
    
    
index_of_divider = data.index("") 
num_of_deques = data[:index_of_divider][-1][-2]
instructions = data[:index_of_divider][:-1]
moves = data[index_of_divider:len(data)][1:]
moves_stack = []
stack = []


for move in moves:
    moves_stack.append(re.match(pattern_for_instructions, move).groups())


for _ in range(int(num_of_deques)):
    stack.append(list())


for instruction in instructions:
    for i, j in enumerate(instruction[1::4]):
        if j != " ":
            stack[i].append(j)
        
    
for m in moves_stack:
    move, from_where, to = m
    stack[int(to)-1].reverse()
    stack[int(to)-1].extend(stack[int(from_where)-1][0:int(move)])
    stack[int(to)-1].reverse()
    del stack[int(from_where)-1][0:int(move)]


final_letters = []
for item in stack:
    final_letters.append(item[0])


print(','.join(final_letters).replace(",", ""))


for m in moves_stack:
    move, from_where, to = m
    stack[int(to)-1].reverse()
    stack[int(to)-1].extend(list(reversed(stack[int(from_where)-1][0:int(move)])))
    stack[int(to)-1].reverse()
    del stack[int(from_where)-1][0:int(move)]
    
final_letters = []
for item in stack:
    final_letters.append(item[0])


print(','.join(final_letters).replace(",", ""))