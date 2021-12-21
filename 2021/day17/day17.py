import re
sample_data = 'x=20..30, y=-10..-5'

with open("2021/day17/input.txt") as file:
    data = file.read()

numbers = re.findall(r'[-]?\d+', sample_data)

input_array = [int(str(number)) for number in numbers]
x_min, x_max, y_max, y_min = input_array

max_possible_point = (y_max*(y_max+1))/2

array_of_x_numbers = []
array_of_all_combinations = []

print(max_possible_point)

def get_step_result(number):
  return (number * (number+1)) / 2

def get_min_acceptable_value():
  for i in range (0, abs(y_max)):
    temp_result = get_step_result(i)
    if temp_result in range(x_min, x_max):
      array_of_x_numbers.append(i)


get_min_acceptable_value()

def check_point_position(x, y):
  down_from_point = (x-y)-1
  down_pos = get_step_result(down_from_point)
  x_pos = get_step_result(x)
  y_pos = get_step_result(y)
  res = y_pos - down_pos
  if res <= get_min_acceptable_value:
    array_of_all_combinations.append((x, y))


def check_x_point_position(x, y):
  total_sum = get_step_result(x)
  diff = x-6
  max_y = y-diff
  point = get_step_result(max_y)
  print(x, y, diff, max_y, point)
  if point < 0:
    array_of_all_combinations.append((x, y))


for i in array_of_x_numbers:
  for j in range(0, abs(y_max)):
    check_point_position(i, j)


# for i in range(array_of_x_numbers[1]+1, x_max):
#   for j in range(0, abs(y_max)):
#     check_x_point_position(i, j)

print(array_of_all_combinations)




