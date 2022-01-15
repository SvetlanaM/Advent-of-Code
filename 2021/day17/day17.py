import re

sample_data = 'x=20..30, y=-10..-5'

with open("2021/day17/input.txt") as file:
    data = file.read()

numbers = re.findall(r'[-]?\d+', data)

input_array = [int(str(number)) for number in numbers]
x_min, x_max, y_max, y_min = input_array
max_possible_point = (y_max*(y_max+1))/2

print("part1:", max_possible_point)
print(x_min)

array_of_x_numbers = []
array_of_all_combinations = []


def get_step_result(number: int) -> int:
  return (number * (number+1)) / 2

def get_min_acceptable_value() -> list(int):
  for i in range (0, abs(y_max)):
    temp_result = get_step_result(i)
    if temp_result in range(x_min, x_max):
      array_of_x_numbers.append(i)


def check_point_position(x: int, y: int) -> list(int):
  down_from_point = (x-y)-1
  down_pos = get_step_result(down_from_point)
  y_pos = get_step_result(y)
  res = y_pos - down_pos
  if res <= max_possible_point:
    array_of_all_combinations.append((x, y))


for i in array_of_x_numbers:
  for j in range(0, abs(y_max)):
    check_point_position(i, j)

get_min_acceptable_value()


def fit_target_area(pos_x: int, pos_y: int, x1: int, y1: int) -> bool:
  x = 0
  y = 0

  while x < max(x1) and y > min(y1):
    x += pos_x
    y += pos_y
    if pos_x > 0:
      pos_x -= 1
    pos_y -= 1

    if x in x1 and y in y1:
            return True

    return False

def find_target() -> int:
    v_x_min = array_of_x_numbers[-1] + 1

 
    v_x_r = range(v_x_min,x_max+ 1)

    v_y_r = range(y_min, y_max)

    print(v_x_r)

    count_of_hits = 0

    for v_x in v_x_r:
        for v_y in v_y_r:
            if fit_target_area(v_x, v_y, x_max, y_max):
                count_of_hits += 1

    print(count_of_hits)
    return count_of_hits


find_target()

