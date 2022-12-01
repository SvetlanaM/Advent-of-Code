def parse_data(file_path: str) -> list[str]:
	with open(file_path, encoding='utf-8') as file:
		return file.read().split('\n\n')


def calculate_calories(data: list[str]) -> list[int]:
	elf_calories = []
	
	for line in data:
		elf_calories.append(sum(list(map(int, line.split()))))
	
	return sorted(elf_calories)

def calculate_max_calories(data: list[str]) -> int:
	return max(calculate_calories(data))

def calculate_top_3(data: list[str]) -> int:
	return sum(calculate_calories(data)[-3:])

def main(file_path: str) -> tuple[int, int]:
	assert calculate_max_calories(parse_data('2022/day01/test_input.txt')) == 24000
	assert calculate_top_3(parse_data('2022/day01/test_input.txt')) == 45000

	input_data = parse_data(file_path)
	max_calories = calculate_max_calories(input_data)
	top_3 = calculate_top_3(input_data)
	return max_calories, top_3


if __name__ == "__main__":
	part_1, part_2 = main("2022/day01/input.txt")
	print(f"Part 1: {part_1}")
	print(f"Part 2: {part_2}")