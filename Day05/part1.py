import re
from collections import defaultdict

with open('input.txt') as fp:
    pattern = re.compile(r'(\d+),(\d+) -> (\d+),(\d+)')
    data = ((int(x) for x in pattern.match(line).groups()) for line in fp.readlines())

board = defaultdict(lambda: defaultdict(int))
for x1, y1, x2, y2 in data:
    if x1 == x2:
        step = 1 if y1 < y2 else -1
        for y in range(y1, y2 + step, step):
            board[x1][y] += 1
    elif y1 == y2:
        step = 1 if x1 < x2 else -1
        for x in range(x1, x2 + step, step):
            board[x][y1] += 1
print(len([x for row in board.values() for x in row.values() if x > 1]))
