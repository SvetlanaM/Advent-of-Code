INPUT_FILE = '2022/day03/test_input.txt'
relative_a = 1
relative_A = ord('A') - 27
combinations = 3


def parse_data(file_path: str) -> list[str]:
    with open(file_path, encoding='utf-8') as file:
        return file.read().splitlines()


def get_converted_dataset(data: list[str]) -> list[tuple[str, ...]]:
    return list(zip(data[0::combinations], data[1::combinations], data[2::combinations]))


def get_score(char: str) -> int:
    return ord(char) - ord('a') + relative_a if char.islower() else ord(char) - relative_A


# at work, i would never do this to anybody :D this python one liners killing me :D
def get_sum_of_priorities(data: list[str]) -> int:
    return sum([get_score(''.join(set(item[:len(item)//2]).intersection(item[len(item)//2:]))) for item in data])


# another killer one liner, next i will do old good multiline for loop
def get_sum_of_3_combinations(data: list[tuple[str, ...]]) -> int:
    return sum([get_score(''.join(set(i1).intersection(i2).intersection(i3))) for i1, i2, i3 in data])


def main(file_path: str) -> tuple[int, int]:
    input_data = parse_data(file_path)
    sum_of_priorities = get_sum_of_priorities(input_data)
    sum_of_3_combinations = get_sum_of_3_combinations(get_converted_dataset(input_data))
    return sum_of_priorities, sum_of_3_combinations


if __name__ == "__main__":
    part_1, part_2 = main(INPUT_FILE.replace("test_", ""))
    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")

 
# tests 
assert get_score('b') == 2
assert get_score('A') == 27
assert get_sum_of_priorities(parse_data(INPUT_FILE)) == 157
assert get_sum_of_3_combinations(get_converted_dataset(parse_data(INPUT_FILE))) == 70