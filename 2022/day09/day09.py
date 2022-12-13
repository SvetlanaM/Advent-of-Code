from enum import Enum

INPUT_FILE = '2022/day09/test_input.txt'


with open(INPUT_FILE, encoding='utf-8') as file:
    data = file.read().strip().splitlines()


class Direction(Enum):
   Up = 'U'
   Down = 'D'
   Right = 'R'
   Left = 'L'
   
    
class Rope:
    head:list[int] = []
    tail:list[int] = []
    visited:list[tuple[int, int]] = [(0, 0)]
    
    
    def __init__(self, head:list[int], tail:list[int]) -> None:
        self.head = head 
        self.tail = tail

    
    def calculate_move(self, to_where:str, distance:int) -> None:
        tail_x, tail_y = self.tail
        
        match to_where:
            case Direction.Up.value:
                self.head[1] += distance
                for i in range(tail_y+1, self.head[1]):
                    self.visited.append((self.head[0], i))
            case Direction.Down.value:
                self.head[1] -= distance
                for i in reversed(range(self.head[1]+1, tail_y)):
                    self.visited.append((self.head[0], i))
            case Direction.Right.value:
                self.head[0] += distance
                for i in range(tail_x+1, self.head[0]):
                    self.visited.append((i, self.head[1]))
            case Direction.Left.value:
                self.head[0] -= distance
                for i in reversed(range(self.head[0]+1, tail_x)):
                    self.visited.append((i, self.head[1]))
            case _:
                raise ValueError(to_where)

    
    def update_last_tail(self) -> None:
        self.tail[0], self.tail[1] = self.visited[-1:][0]
    
            
    def move(self, line: str) -> None:        
        to_where, distance = line.split(" ")
        
        tail = self.tail.copy()
        self.calculate_move(to_where=to_where, distance=int(distance))
        head = self.head.copy()
        
        head_x, head_y, tail_x, tail_y = *head, *tail

        if max(abs(head_x - tail_x), abs(head_y - tail_y)) >= 2:
            self.update_last_tail()
    
       
    def print_result(self) -> None:
        print(len(set(self.visited)))
        
            
r = Rope(head=[0, 0], tail=[0,0])
for line in data:
    r.move(line)
    
r.print_result()
    
    
               
        
