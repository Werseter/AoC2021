with open('input.txt') as fp:
    data = (x.split() for x in fp.readlines())
    data = ((a, int(b)) for a, b in data)
aim, depth, position = 0, 0, 0
for command, value in data:
    match command:
        case 'forward':
            position += value
            depth += aim * value
        case 'down':
            aim += value
        case 'up':
            aim -= value
print(position * depth)
