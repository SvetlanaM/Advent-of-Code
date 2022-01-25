with open("2015/day03/input.txt") as file:
    data:str = file.read().splitlines()[0]

moves: dict[str, int] = {'^' : 1, 'v' : -1, '>' : 1, '<': -1}

def part1(data:str) -> int:
    coordinations:list = []
    x, y = 0, 0
    coordinations.append((x, y))
    for move in data:
        if move in ['^', 'v']:
            x += moves[move]
        else:
            y += moves[move]
        coordinations.append((x, y))
    return len(set(coordinations)), coordinations


def part2() -> int:
    santa_instructions:str = data[::2]
    robo_santa_instructions:str = data[1::2]
    _, santas = part1(santa_instructions)
    _, robos = part1(robo_santa_instructions)
    return len(set(santas + robos))

print("Part1", part1(data)[0])
print("Part2", part2())