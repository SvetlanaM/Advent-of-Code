import re 

with open("2021/day14/input.txt", encoding='utf-8') as file:
    data = file.read().split("\n")

index_of_divider = data.index("")
input_word = data[0:index_of_divider]
instructions = data[index_of_divider+1: len(data)]
instruction_dict = {}

for instruction in instructions:
    i = instruction.split(' -> ')
    instruction_dict[i[0]] = i[0][0] + i[1] + i[0][1]


pattern = re.compile('|'.join(r'(?=(' + key + r'))' for key in instruction_dict.keys() if key != ' '))
new_word = input_word[0]

for j in range(0, 10):
    print(new_word)
    for i in range(1,4):
        res = re.sub(pattern, lambda x: instruction_dict[x.group(i)], new_word[i-1:i+1])
        new_word += res[0:2]

print(new_word)