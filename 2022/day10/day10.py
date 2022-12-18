import re 
INPUT_FILE = '2022/day10/test_input.txt'

CPU_cycles = []

def parse_data(file_path: str) -> list[str]:
    with open(file_path, encoding='utf-8') as file:
        return file.read().strip().splitlines()


def generate_cycle_list(data: list[str]) -> list[int]:
    for line in data:
        if line[-1].isdigit():
            CPU_cycles.extend([0, int(re.findall('-?\d+', line)[0])])
        else:
            CPU_cycles.append(0)
    
    return CPU_cycles
        
def calculate_sum_of_cpu_cycles(cpu_cycles: list[int]) -> int:
    current_index = 20
    cumulated_sums = []
    
    for _ in cpu_cycles[20::40]:
        total_sum = 1
        total_sum += sum(cpu_cycles[:current_index-1])
        cumulated_sums.append(total_sum * current_index)
        current_index += 40
    
    return sum(cumulated_sums) 

def render_crt_image(cpu_cycles: list[int]) -> None:
    crt = [["░"] * 40 for _ in range(6)]
    iteration = 0
    current_index = 40
    
    for cycle in range(len(cpu_cycles)):
        _ = sum(cpu_cycles[:cycle]) + 1
        if cycle % 40 in range(_-1, _+2):
            crt[iteration][cycle%40] = '▓'
        
        if cycle > current_index-2:
            iteration += 1
            current_index += 40
        
    for line in crt:
        print("".join([c for c in line]))
 
   
def main(file_path: str) -> None:
    input_data = parse_data(file_path)
    cpu_cycles = generate_cycle_list(input_data)
    sum_of_cpu_cycles = calculate_sum_of_cpu_cycles(cpu_cycles)
    print("Part 1:", "Total sum of CPU cycles is", sum_of_cpu_cycles)
    print("Part 2: Rendered CRT image is")
    render_crt_image(cpu_cycles)
    
    
if __name__ == "__main__":
    raise SystemExit(main(INPUT_FILE.replace("test_", "")))