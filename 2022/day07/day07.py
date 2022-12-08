from functools import reduce
import re
from dataclasses import dataclass

INPUT_FILE = '2022/day07/test_input.txt'

@dataclass
class Directory:
    name: str
    size: int
    

def parse_data(file_path: str) -> list[str]:
    with open(file_path, encoding='utf-8') as file:
        return file.read().splitlines()

def list_of_directories(data: list[str]) -> list[Directory]:
    directories:list[Directory] = []
    parents:list[Directory] = []

    for command in data:
        if '$ cd ..' == command:
            directories.append(parents.pop())
        elif '..' not in command and '$ cd' in command:
            dir_name = command.rsplit(' ', 1)[1]
            parents.append(Directory(dir_name, 0))
        elif 'dir' not in command:
            if len(re.findall('\d+', command)) != 0:
                file_size = re.findall('\d+', command)[0]
                for parent in parents:
                    parent.size += int(file_size)
        else:
            pass
        
    directories += parents
    return directories


def compute_total_disk_space(directories: list[Directory]) -> int:
    less = list(filter(lambda elem: elem.size <= 100000, directories))
    return reduce(lambda a, b: a + b, list(map(lambda a: a.size, less)))



def find_folder_size_for_deletion(directories: list[Directory]) -> int:
    outermost_value = list(filter(lambda a: a.name == '/', directories))[0].size
    space_needed = 70000000 - outermost_value
    space_to_free = 30000000 - space_needed
    big_directories = list(filter(lambda a: a.size > space_to_free, directories))
    return reduce(lambda a, b: min(a, b), list(map(lambda a: a.size, big_directories)))


# tests 
assert compute_total_disk_space(list_of_directories(parse_data(INPUT_FILE))) == 95437
assert find_folder_size_for_deletion(list_of_directories(parse_data(INPUT_FILE))) == 24933642 


def main(file_path: str) -> None:
    input_data = parse_data(file_path)
    directories = list_of_directories(input_data)
    total_disk_space, folder_size_to_delete = compute_total_disk_space(directories), find_folder_size_for_deletion(directories)
    print("Part 1:", total_disk_space)
    print("Part 2:", folder_size_to_delete)
    
    
if __name__ == "__main__":
    raise SystemExit(main(INPUT_FILE.replace("test_", "")))

