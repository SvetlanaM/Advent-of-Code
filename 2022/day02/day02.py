from itertools import product

INPUT_FILE = '2022/day02/test_input.txt'

# shape score
ROCK = 1
PAPER = 2 
SCISSORS = 3

# round result
LOST = 0
DRAW = 3
WIN = 6

game_combinations = {}
combinations = list(product('ABC', ['X', 'Y', 'Z']))
mapping_dict = {'A' : ROCK, 'B' : PAPER, 'C': SCISSORS, 'X': ROCK, 'Y' : PAPER, 'Z' : SCISSORS}
end_round_dict = {'X' : 'LOST', 'Y' : 'DRAW', 'Z' : 'WIN', 'A' : 'ROCK', 'B' : 'PAPER', 'C' : 'SCISSORS'}

def parse_data(file_path: str) -> list[str]:
    with open(file_path, encoding='utf-8') as file:
        data = file.read().splitlines()
        return [line.replace(" ", "") for line in data]


def get_end_round_result(shape: str) -> int:
    oponent, mine = end_round_dict.get(shape[0]), end_round_dict.get(shape[1])
    
    # i was lazy here, maybe in the future use tuple combinations or switch 
    if mine == 'WIN':
        if oponent == 'ROCK':
            return PAPER + WIN
        if oponent == 'SCISSORS':
            return ROCK + WIN
        if oponent == 'PAPER':
            return SCISSORS + WIN
        
    if mine == 'LOST':
        if oponent == 'PAPER':
            return ROCK + LOST
        if oponent == 'ROCK':
            return SCISSORS + LOST
        if oponent == 'SCISSORS':
            return PAPER + LOST
        
    if mine == 'DRAW':
        return mapping_dict.get(shape[0]) + DRAW


def get_round_result(shape: str) -> int:
    oponent, mine = mapping_dict.get(shape[0]), mapping_dict.get(shape[1])
    
    # i dont like ifs :D really
    if mine == oponent:
        return DRAW
    
    if mine == ROCK and oponent == SCISSORS:
        return WIN
    
    if mine == SCISSORS and oponent == PAPER:
        return WIN
    
    if mine == PAPER and oponent == ROCK:
        return WIN
    
    return LOST


def generate_combinations(combinations: list[str] = combinations) -> dict[str, int]: 
    for c in combinations:
        game_combinations[c[0] + c[1]] = mapping_dict.get(c[1]) + get_round_result(c[0] + c[1])
        

def compute_end_game_result(data: list[str]) -> int:
    return sum([get_end_round_result(line) for line in data])


def compute_game_result(data: list[str]) -> int:
    generate_combinations()
    return sum([game_combinations[line] for line in data])


def main(file_path: str) -> tuple[int, int]:
    assert compute_game_result(parse_data(INPUT_FILE)) == 15
    assert compute_end_game_result(parse_data(INPUT_FILE)) == 12
    
    input_data = parse_data(file_path)
    result = compute_game_result(input_data)
    end_game_result = compute_end_game_result(input_data)
    return result, end_game_result


if __name__ == "__main__":
    part_1, part_2 = main(INPUT_FILE.replace("test_", ""))
    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")
 

