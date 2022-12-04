import re 

INPUT_FILE = '2022/day04/test_input.txt'
pattern_for_instructions = '^(\d+)-(\d+)'


def parse_data(file_path: str) -> list[str]:
    with open(file_path, encoding='utf-8') as file:
        data = file.read().splitlines()
        return [line.split(',') for line in data]


def convert_dataset(section: list[str]) -> tuple[list[int], list[int]]:
    section1, section2 = re.match(pattern_for_instructions, section[0]).groups(), \
                         re.match(pattern_for_instructions, section[1]).groups()
    s1_list = list(range(int(section1[0]), int(section1[1]) + 1))
    s2_list = list(range(int(section2[0]), int(section2[1]) + 1))
    return s1_list, s2_list
        

# today, no one liners
def get_sum_of_pairs(sections: list[list[str]]) -> int:
    sum_of_overlap = 0

    for section in sections:
        s1_list, s2_list = convert_dataset(section)
        if set(s1_list).issubset(s2_list) or set(s2_list).issubset(s1_list):
            sum_of_overlap += 1
    
    return sum_of_overlap


def get_single_overlap(sections: list[list[str]]) -> int:
    sum_of_overlap = 0
    
    for section in sections:
        s1_list, s2_list = convert_dataset(section)
        if len(set(s1_list).intersection(s2_list)) > 0:
            sum_of_overlap += 1
            
    return sum_of_overlap
    

def main(file_path: str) -> tuple[int, int]:
    input_data = parse_data(file_path)
    sum_of_pairs = get_sum_of_pairs(input_data)
    sum_of_single = get_single_overlap((input_data))
    return sum_of_pairs, sum_of_single


if __name__ == "__main__":
    part_1, part_2 = main(INPUT_FILE.replace("test_", ""))
    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")