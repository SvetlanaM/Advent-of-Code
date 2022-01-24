with open("2015/day03/input.txt") as file:
    data = file.read().splitlines()[0]


def part1(data):
    coordinations = []
    x, y = 0, 0
    coordinations.append((x, y))
    for move in data:
        if move == '^':
            x += 1
            coordinations.append((x, y))
        if move == 'v':
            x -= 1
            coordinations.append((x, y))
        if move == '>':
            y += 1
            coordinations.append((x, y))
        if move == '<':
            y -= 1
            coordinations.append((x, y))
    return len(set(coordinations)), coordinations


def part2():
    santa_instructions = []
    robo_santa_instructions = []
    for i, move in enumerate(data):
        if i % 2 == 0:
            santa_instructions.append(move)
        else:
            robo_santa_instructions.append(move)
    _, santas = part1(santa_instructions)
    _, robos = part1(robo_santa_instructions)
    return len(set(santas + robos))

print("Part1", part1(data)[0])
print("Part2", part2())