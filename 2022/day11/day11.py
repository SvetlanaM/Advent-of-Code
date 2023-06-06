from collections import deque
from dataclasses import dataclass, field
from functools import reduce
import operator

INPUT_FILE = '2022/day11/test_input.txt'

@dataclass
class Monkey:
    starting_items: dict = field(default_factory=dict[int, list[int]])
    final_items: dict = field(default_factory=dict[int, list[int]])
    

with open(INPUT_FILE, encoding='utf-8') as file:
    data = file.read().splitlines()
    
monkeys:list[Monkey] = []

operators = {
    '*': operator.mul,
    '+': operator.add
}

for line in data:
    command = line.split()
    # print(command)
    match command:
        case 'Monkey', number:
            monkeys.insert(0, Monkey())
        case 'Starting', 'items:', *items:
            monkeys[0].starting_items[number] = [int(item.replace(",", "")) for item in items]
        case 'Operation:', 'new', '=',  'old', operator_type, number:
            temp_arr:list = []
            for item in monkeys[0].starting_items.values():
                print(monkeys[0].starting_items.values())
                if number != 'old':
                    if operator_type == '+':
                        calc = number + item
                    
                    if operator_type == '*':
                        calc = number * item 
                        
                    temp_arr.append(calc)
                else:
                    if operator_type == '+':
                        calc = item + item
                    
                    if operator_type == '*':
                        calc = item * item
                        
                    temp_arr.append(calc)
        case 'Test:', 'divisible', 'by', number:
            divisible_arr:dict = {}
            for item in temp_arr:
                print(item)
                item //= 3
                if item % number == 0:
                    divisible_arr[item] = True
                else:
                    divisible_arr[item] = False
        case 'If', 'true:' 'throw', 'to', 'monkey', number:
            for key, value in divisible_arr.items():
                if value == True:
                    monkeys[0].final_items[number] = key
                    
                    
                
            
            