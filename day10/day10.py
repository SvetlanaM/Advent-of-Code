with open("day10/input.txt", encoding='utf-8') as file:
    data = file.read().splitlines()

opening_chars = '([{<'
closing_chars = ')]}>'
sum_of_corrupted = 0
mapping_dict = {'(' : [')', 3], '[' : [']', 57], '{' : ['}', 1197], '<' : ['>', 25137]}
mapping_dict_sums = {')' : 3, ']' : 57, '}' : 1197, '>' :  25137}


for line in data:
    print(line)
    empty_array = []
    for key, char in enumerate(line):
        print(key, char, empty_array)
        if char in closing_chars:
            last_char = empty_array.pop(-1)   
            if char != mapping_dict[last_char][0]:
                print(last_char, mapping_dict[last_char][0])
                sum_of_corrupted += mapping_dict_sums[char]
                break
        else:
            empty_array.insert(len(empty_array), char)

print(sum_of_corrupted)
               