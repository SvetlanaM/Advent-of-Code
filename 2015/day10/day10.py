import re

pattern_for_instructions = r'(\d)\1*'
pattern_object = re.compile(pattern_for_instructions)

def compute(num_of_repeat:int, exp_number:str = '1113122113') -> int:
  for _ in range(num_of_repeat):
    matched_group = pattern_object.finditer(exp_number)
    exp_number = ''
    for m in matched_group:
      exp_number += str(len(m.group())) + m.groups()[0]
  return len(exp_number)
  
print("Part 1:", compute(40))
print("Part 2:", compute(50))