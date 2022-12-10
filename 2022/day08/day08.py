INPUT_FILE = '2022/day08/test_input.txt'


def parse_data(file_path: str) -> list[str]:
    with open(file_path, encoding='utf-8') as file:
        return file.read().splitlines()

  
def generate_grid(data: list[str]) -> tuple([list[int], list[int]]):
    rows = list([list(map(int, x)) for x in [list(word) for word in data]])
    cols = list(list(zip(*rows)))
    return rows, cols


def move_on_grid(rows: list[int], columns: list[int], row_index: int, col_index: int) -> dict[str: list[int]]:
    right = rows[row_index][:col_index]
    left = rows[row_index][col_index+1:]
    up = columns[col_index][:row_index]
    down = columns[col_index][row_index+1:]
    
    return {'right': right, 'left': left, 'up': up, 'down': down}


def calculate_sum_of_visible_trees(forrest: dict[str: list[int]]) -> int:
    rows, columns = forrest
    num_of_visibles = 0
    
    for row_index, row in enumerate(rows):
        for col_index, col in enumerate(row):
            current_height = col
            forrest_dict = move_on_grid(rows, columns, row_index, col_index)
            
            try:
                if any(max(x) < current_height for x in forrest_dict.values()):
                    num_of_visibles += 1
            except ValueError:
                num_of_visibles += 1 # ignore this hack :D i am also lazy programmer 
                continue
            
    return num_of_visibles


def calculate(height: int, arr: list[int]) -> int:
    count = 0
    for i in arr:
        count += 1
        if i >= height:
            break
        
    return count


def calculate_highest_view(forrest: dict[str: list[int]]) -> int:
    rows, columns = forrest
    max_distance = 0
    
    for row_index, row in enumerate(rows):
        for col_index, col in enumerate(row):
            current_height = col
            forrest_dict = move_on_grid(rows, columns, row_index, col_index)
            
            distance_to_right = calculate(current_height, reversed(forrest_dict['right']))
            distance_to_left = calculate(current_height, forrest_dict['left'])
            distance_to_top = calculate(current_height, reversed(forrest_dict['up']))
            distance_to_down = calculate(current_height, forrest_dict['down'])
            if total_distance := distance_to_right * distance_to_left * distance_to_top * distance_to_down:
                max_distance = max(total_distance, max_distance)
            
    return max_distance


#tests
def test() -> None:
    assert calculate_sum_of_visible_trees(generate_grid(parse_data(INPUT_FILE))) == 21
    assert calculate_highest_view(generate_grid(parse_data(INPUT_FILE))) == 8


def main(file_path: str) -> None:
    test()
    
    input_data = parse_data(file_path)
    forrest = generate_grid(input_data)
    num_of_visible_trees = calculate_sum_of_visible_trees(forrest)
    best_view = calculate_highest_view(forrest)
    print("Part 1:", num_of_visible_trees)
    print("Part 2:", best_view)
    
    
if __name__ == "__main__":
    raise SystemExit(main(INPUT_FILE.replace("test_", "")))
