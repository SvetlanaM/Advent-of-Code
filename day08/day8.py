with open("day08/input_8.txt", encoding='utf-8') as file:
    data = file.read().splitlines()

test_data = {'abcdeg': 6, 'abcfg': 3, 'bcdf': 4, 'abdefg': 0, 'abcdg': 5, 'abcdefg': 8, 'acefg': 2, 'abcdfg': 9, 'abf': 7, 'bf': 1}

input_data_first = [item.split("|")[1].strip() for item in data]
input_data_second = [item for item in data]
input_values = [2, 3, 4, 7]
input_values_dict = {2:1, 3:7, 4:4, 7:8}
number_of_oc = []


def part_one():
    sum_of_values = 0
    for row in input_data_first:
        array_row = row.split(" ")
        for item in array_row:
            if len(item) in input_values:
                sum_of_values += 1
    return sum_of_values

def sort_by_char(input:str) -> str:
    return ''.join(sorted(input))

def get_by_size(dict, size):
    return [s for s in dict if len(s) == size]

def find_substring(string, substring, stop=None):
    count = 0
    max_count = len(substring)
    for s in substring:
        if s in string:
            count += 1
            if count == max_count or count == stop:
                return True
            

def part_two():
    for value in input_data_second:
        new_mapping_dict = {}
        left_side = value.split("|")[0].strip().split(" ")
        right_side = value.split("|")[1].strip().split(" ")
        
        for string in left_side:
            if len(string) in input_values:
                new_mapping_dict[sort_by_char(string)] = input_values_dict[len(string)]
            elif len(string) == 6:
                if find_substring(string, get_by_size(left_side, 4)[0]):
                    new_mapping_dict[sort_by_char(string)] = 9
                elif find_substring(string, get_by_size(left_side, 2)[0]):
                    new_mapping_dict[sort_by_char(string)] = 0
                else:
                    new_mapping_dict[sort_by_char(string)] = 6
            elif len(string) == 5:
                if find_substring(string, get_by_size(left_side, 3)[0]):
                    new_mapping_dict[sort_by_char(string)] = 3
                elif find_substring(string, get_by_size(left_side, 4)[0], 3):
                    new_mapping_dict[sort_by_char(string)] = 5
                elif find_substring(get_by_size(left_side, 7)[0], string):
                    new_mapping_dict[sort_by_char(string)] = 2
            
        
        c = 0
        final_number = ""
        for right_value in right_side:
            if sort_by_char(right_value) in new_mapping_dict.keys():
                final_number = final_number + str(new_mapping_dict[sort_by_char(right_value)])
            if c == 3:
                number_of_oc.append(final_number)
            c += 1
            
    
    return sum([int(line) for line in number_of_oc])

print("Part", part_one())
print("Part", part_two())

