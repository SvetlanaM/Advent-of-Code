
import math

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

    def explode(self, depth = 1):
        if depth > 4:
            if self.left_neighbour is not None:
                if self.left_neighbour.right_literal is not None:
                    self.left_neighbour.right_literal += self.left_literal
                elif self.left_neighbour.left_literal is not None:
                    self.left_neighbour.left_literal += self.left_literal
            
                if self.left_neighbour == self.parent:
                    self.parent.right_neighbour = self.right_neighbour
                else:
                    self.left_neighbour.right_neighbour = self.parent
                
            if self.right_neighbour is not None:
                if self.right_neighbour.left_literal is not None:
                    self.right_neighbour.left_literal += self.right_literal
                elif self.right_neighbour.right_literal is not None:
                    self.right_neighbour.right_literal += self.right_literal
            
                if self.right_neighbour == self.parent:
                    self.parent.left_neighbour = self.left_neighbour
                else:
                    self.right_neighbour.left_neighbour = self.parent
            
            if self.parent.left_pair == self:
                self.parent.left_pair = None
                self.parent.left_literal = 0
            elif self.parent.right_pair == self:
                self.parent.right_pair = None 
                self.parent.right_literal = 0
        
        if self.left_pair is not None:
            self.left_pair.explode(depth + 1)
        if self.right_pair is not None:
            self.right_pair.explode(depth + 1)
            
    def split_left(self):
        self.left_pair = Pair(self)
        self.left_pair.left_literal = math.floor(self.left_literal/2)
        self.left_pair.right_literal = math.ceil(self.left_literal/2)
        self.left_literal = None

        if self.left_neighbour is not None:
            self.left_pair.left_neighbour = self.left_neighbour
            self.left_neighbour.right_neighbour = self.left_pair

        if self.right_pair is not None:
            self.left_pair.right_neighbour = self.right_neighbour
            self.right_neighbour.left_neighbour = self.left_pair
        else:
            self.left_pair.right_neighbour = self
            self.left_neighbour = self.left_pair

    def split_right(self):
        self.right_pair = Pair(self)
        self.right_pair.left_literal = math.floor(self.right_literal/2)
        self.right_pair.right_literal = math.ceil(self.right_literal/2)
        self.right_literal = None

        if self.right_neighbour is not None:
            self.right_pair.right_neighbour = self.right_neighbour
            self.right_neighbour.left_neighbour = self.right_pair

        if self.left_pair is not None:
            self.right_pair.left_neighbour = self.left_neighbour
            self.left_neighbour.right_neighbour = self.right_pair
        else:
            self.right_pair.left_neighbour = self
            self.right_neighbour = self.right_pair

    def split(self, depth = 1):
        if self.left_literal is not None and int(self.left_literal) > 9:
            self.split_left()
            self.explode(depth)
            return True

        if self.left_pair is not None:
            if self.left_pair.split(depth + 1):
                return True

        if self.right_literal is not None and int(self.right_literal) > 9:
            self.split_right()
            self.explode(depth)
            return True

        if self.right_pair is not None:
            if self.right_pair.split(depth + 1):
                return True
        
        return False

    def reduce_number(self):
        self.show_print()
        print('')
        self.explode()
        self.show_print()
        print('')
        while self.split():
            self.show_print()
            print("")
            pass
        
    def first_pair(self):
        if self.left_literal is not None:
            return self
        else:
            return self.left_pair.first_pair()

    def last_pair(self):
        if self.right_literal is not None:
            return self
        else:
            return self.right_pair.last_pair()

    def __add__(self, o):
        new_root = Pair(None)
        new_root.left_pair = self
        new_root.right_pair = o

        last_neighbour = self.last_pair()
        first_neighbour = o.first_pair()
        last_neighbour.right_neighbour = first_neighbour
        first_neighbour.left_neighbour = last_neighbour

        self.parent = new_root
        o.parent = new_root
        return new_root

    def show_print(self):
        print("[", end ="")
        if self.left_literal is not None:
            print(self.left_literal, end ="")
        elif self.left_pair is not None:
            self.left_pair.show_print()
        print(",", end ="")
        if self.right_literal is not None:
            print(self.right_literal, end ="")
        elif self.right_pair is not None:
            self.right_pair.show_print()     
        print("]", end ="")

    def calculate_magnitude(self):
        final_sum = 0
        if self.left_pair is not None:
            final_sum += self.left_pair.calculate_magnitude() * 3
        if self.right_pair is not None:
            final_sum += self.right_pair.calculate_magnitude() * 2
        if self.left_literal is not None:
            final_sum += self.left_literal * 3
        if self.right_literal is not None:
            final_sum += self.right_literal * 2
        
        return final_sum

        

def create_pair(pair: Pair, input: str, last_pair: Pair):

    if input[0] == '[':
        pair.left_pair = Pair(pair)
        input, last_pair = create_pair(pair.left_pair, input[1:], last_pair)
    else:
        pair.left_literal = int(input[0])
        pair.left_neighbour = last_pair
        if last_pair is not None:
            last_pair.right_neighbour = pair
        last_pair = pair

    input = input.split(",", 1)[1]
    
    if input[0] == '[':
        pair.right_pair = Pair(pair)
        input, last_pair = create_pair(pair.right_pair, input[1:], last_pair)
    else:
        pair.right_literal = int(input[0])
        if pair.left_pair != None:
            pair.left_neighbour = last_pair
            if last_pair is not None:
                last_pair.right_neighbour = pair
            last_pair = pair
     
    return input[1:], last_pair




first_root = Pair(None)
create_pair(first_root, data[0][1:-1], None)

for i in range(len(data)-1):
    second_root = Pair(None)
    create_pair(second_root, data[i+1][1:-1], None)
    first_root += second_root
    first_root.reduce_number()

print(first_root.calculate_magnitude())

max = 0

new_data = data.copy()
for a, b in enumerate(new_data):
    data.sort(key=b.__eq__)
    for i in range(len(data)-1):
        print(i)
        temp = 0
        first_root = Pair(None)
        create_pair(first_root, b[1:-1], None)
        second_root = Pair(None)
        create_pair(second_root, data[i][1:-1], None)
        first_root += second_root
        first_root.reduce_number()
        temp = first_root.calculate_magnitude()
        if temp > max:
            max = temp
    
print("max", max)