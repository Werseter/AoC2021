def floodfill(idx_x: int, idx_y: int):
    total = 0
    if data[idx_y][idx_x] != 9:
        data[idx_y][idx_x] = 9
        total += 1
        total += floodfill(idx_x - 1, idx_y) if idx_x > 0 else 0
        total += floodfill(idx_x + 1, idx_y) if idx_x < len(data[0]) - 1 else 0
        total += floodfill(idx_x, idx_y - 1) if idx_y > 0 else 0
        total += floodfill(idx_x, idx_y + 1) if idx_y < len(data) - 1 else 0
    return total


with open('input.txt') as fp:
    data = [[int(y) for y in x.strip()] for x in fp.readlines()]
tmp = [[floodfill(idx_x, idx_y) for idx_x in range(len(y))] for idx_y, y in enumerate(data)]
acc = 1
print([acc := acc * v for v in sorted((elem for row in tmp for elem in row if elem != 0), reverse=True)[:3]][-1])
