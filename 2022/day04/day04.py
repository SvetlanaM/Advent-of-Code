import re 

INPUT_FILE = '2022/day04/test_input.txt'

def parse_data(file_path: str) -> list[str]:
    with open(file_path, encoding='utf-8') as file:
        data = file.read().splitlines()
        return [line.split(',') for line in data]


def convert_dataset(section: list[str]) -> tuple[set[int], set[int]]:
    section1, section2 = re.findall('\d+', section[0]), re.findall('\d+', section[1])
    s1 = set(range(int(section1[0]), int(section1[1]) + 1))
    s2 = set(range(int(section2[0]), int(section2[1]) + 1))
    return s1, s2
        

# today, no one liners
def get_sum_of_pairs(sections: list[list[str]]) -> tuple[int, int]:
    sum_of_overlap = 0
    sum_of_unique = 0
    
    for section in sections:
        s1, s2 = convert_dataset(section)
        
        if s1.issubset(s2) or s2.issubset(s1):
            sum_of_overlap += 1
        
        if len(s1.intersection(s2)) > 0:
            sum_of_unique += 1
    
    return sum_of_overlap, sum_of_unique
    

def main(file_path: str) -> tuple[int, int]:
    input_data = parse_data(file_path)
    sum_of_pairs, sum_of_single = get_sum_of_pairs(input_data)
    return sum_of_pairs, sum_of_single


if __name__ == "__main__":
    part_1, part_2 = main(INPUT_FILE.replace("test_", ""))
    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")

   
# tests 
assert convert_dataset(['2-4', '6-8']) == ({2, 3, 4}, {6, 7, 8})
assert get_sum_of_pairs(parse_data(INPUT_FILE))[0] == 2
assert get_sum_of_pairs(parse_data(INPUT_FILE))[1] == 4