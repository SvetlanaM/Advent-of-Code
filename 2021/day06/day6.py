from collections import Counter
from collections import OrderedDict
import time
start_time = time.time()

with open("input_6.txt", encoding='utf-8') as file:
    data = file.read().splitlines()[0].split(",")

data = [int(line) for line in data]

def task6():
    ordered_dict = OrderedDict()
    fishCounter = Counter()
    for item in data:
        fishCounter[item] += 1
    
    converted_dict = dict(fishCounter)
    
    for i in range(0,9):
        if i not in converted_dict:
            converted_dict[i] = 0
    
    for key, value in sorted (converted_dict.items(), reverse=False) :
        ordered_dict[key] = value    

    for i in range(0,256):
        temp_value = 0
        for key, value in ordered_dict.items():
            if key == 0:
                temp_value = value
                ordered_dict[key] = ordered_dict[key+1]
            if key == 8:
                ordered_dict[6]  += temp_value
                ordered_dict[8] = temp_value
            else:
                ordered_dict[key] = ordered_dict[key+1]

    print(sum(ordered_dict.values()))
    print("Process finished %s seconds" % (time.time() - start_time))
    

task6()
