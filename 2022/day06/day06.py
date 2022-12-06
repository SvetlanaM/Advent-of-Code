import collections
from itertools import islice
from typing import Iterable

INPUT_FILE = '2022/day06/test_input.txt'


def parse_data(file_path: str) -> str:
    with open(file_path, encoding='utf-8') as file:
        return file.read()

# function from here - https://docs.python.org/3/library/itertools.html    
def sliding_window(iterable: Iterable, n: int) -> Iterable:
    # sliding_window('ABCDEFG', 4) --> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)
        

def compute(data: str, position: int = 4) -> int:
    for index, window in enumerate(sliding_window(data, position)):
        if len(set(window)) == position:
            return index + position

# tests 
assert compute('bvwbjplbgvbhsrlpgdmjqwftvncz') == 5
assert compute('nppdvjthqldpwncqszvftbrmjlhg') == 6
assert compute('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 11  
assert compute('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 14) == 26 


def main(file_path: str) -> None:
    input_data = parse_data(file_path)
    num_of_chars = compute(input_data)
    num_of_chars_2 = compute(input_data, 14)
    print("Part 1:", num_of_chars)
    print("Part 2:", num_of_chars_2)
    
    
if __name__ == "__main__":
    raise SystemExit(main(INPUT_FILE.replace("test_", "")))
    