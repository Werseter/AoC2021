from bisect import insort

with open('input.txt') as fp:
    data = [[int(y) for y in x.strip()] for x in fp.readlines()]
paths = [(0, 0, 0)]
shortest_paths = {(0, 0): 0}
while True:
    idx_x, idx_y, dist = paths.pop(0)
    if idx_x == idx_y == len(data) - 1:
        break
    for shift_x, shift_y in (0, -1), (1, 0), (0, 1), (-1, 0):
        new_idx_x, new_idx_y = idx_x + shift_x, idx_y + shift_y
        if not any(x < 0 or x >= len(data) for x in (new_idx_x, new_idx_y)):
            if (new_idx_x, new_idx_y) not in shortest_paths:
                shortest_paths[(new_idx_x, new_idx_y)] = (new_dist := dist + data[new_idx_y][new_idx_x])
                insort(paths, (new_idx_x, new_idx_y, new_dist), key=lambda x: x[2])
print(dist)
