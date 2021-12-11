with open("day10/input.txt", encoding='utf-8') as file:
    data = file.read().splitlines()

opening_chars = '([{<'
closing_chars = ')]}>'
sum_of_corrupted = 0
mapping_dict = {'(' : [')', 3], '[' : [']', 57], '{' : ['}', 1197], '<' : ['>', 25137]}
mapping_dict_sums = {')' : 3, ']' : 57, '}' : 1197, '>' :  25137}
mapping_dict_part2 = {'(' : 1, '[' : 2, '{' : 3, '<' :  4}
total_points = []

for line in data:
    empty_array = []
    for key, char in enumerate(line):
        if char in closing_chars:
            last_char = empty_array.pop(-1)   
            if char != mapping_dict[last_char][0]:
                empty_array = []
                break
        else:
            empty_array.insert(len(empty_array), char)
    
    acc = 0
    for score in empty_array[::-1]:
        acc = acc * 5 + mapping_dict_part2[score]
    
    if len(empty_array) != 0:
        total_points.append(acc)


middle_key = int(len(total_points)/2)
middle_score = sorted(total_points)[middle_key]
print(middle_score)
               