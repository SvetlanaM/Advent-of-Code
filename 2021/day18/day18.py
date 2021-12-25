
with open("2021/day18/input.txt") as file:
    data = file.read().splitlines()



class Pair:
    left_literal = None
    left_pair = None 
    right_literal = None
    right_pair = None
    right_neighbour = None
    left_neighbour = None
    

    def __init__(self, parent):
        self.parent = parent

    def reduce_number(depth:int = 1):
        if depth > 4:
            pass


    def __add__(self, o):
        new_root = Pair(None)
        new_root.left_pair = self
        new_root.right_pair = o
        self.parent = new_root
        o.parent = new_root
        return new_root

    def show_print(self):
        print("[", end ="")
        if self.left_literal is not None:
            print(self.left_literal, end ="")
        elif self.left_pair is not None:
            self.left_pair.show_print()
            if self.left_neighbour is not None:
                self.left_neighbour.show_print()
        print(",", end ="")
        if self.right_literal is not None:
            print(self.right_literal, end ="")
        elif self.right_pair is not None:
            self.right_pair.show_print()
            if self.right_neighbour is not None:
                self.right_neighbour.show_print()
        print("]", end ="")
        

def create_pair(pair: Pair, input: str, last_pair: Pair):

    if input[0] == '[':
        pair.left_pair = Pair(pair)
        input = create_pair(pair.left_pair, input[1:], None)[0]
    else:
        pair.left_literal = input[0]
        pair.left_neighbour = last_pair
        last_pair = create_pair(last_pair, input[1:], pair)[1]
    

    input = input.split(",", 1)[1]
    
    if input[0] == '[':
        pair.right_pair = Pair(pair)
        input = create_pair(pair.right_pair, input[1:], last_pair)[0]
    else:
        pair.right_literal = input[0]
     
    return input[1:], last_pair



first_root = Pair(None)
second_root = Pair(None)

pair = create_pair(first_root, data[0][1:-1], first_root)
pair1 = create_pair(second_root, data[1][1:-1], second_root)


actual_row = first_root + second_root

print(actual_row.show_print())
