with open('input.txt') as fp:
    data = (x.split() for x in fp.readlines())
    data = ((a, int(b)) for a, b in data)
depth, position = 0, 0
for command, value in data:
    match command:
        case 'forward':
            position += value
        case 'down':
            depth += value
        case 'up':
            depth -= value
print(position * depth)
