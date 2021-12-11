def step(idx_x: int, idx_y: int) -> None:
    if not any(x < 0 or x >= len(data) for x in (idx_x, idx_y)) and data[idx_y][idx_x] != -1:
        data[idx_y][idx_x] += 1


def burst(idx_x: int, idx_y: int) -> None:
    if data[idx_y][idx_x] > 9:
        data[idx_y][idx_x] = -1
        for x_shift in range(-1, 2):
            for y_shift in range(-1, 2):
                step(idx_x + x_shift, idx_y + y_shift)


def reset(idx_x: int, idx_y: int) -> int:
    if data[idx_y][idx_x] == -1:
        data[idx_y][idx_x] = 0
    return 1 if data[idx_y][idx_x] == 0 else 0


with open('input.txt') as fp:
    data = [[int(y) for y in x.strip()] for x in fp.readlines()]
counter = 0
for _ in range(100):
    [[step(idx_x, idx_y) for idx_x, x in enumerate(y)] for idx_y, y in enumerate(data)]
    while [elem for row in data for elem in row if elem > 9]:
        [[burst(idx_x, idx_y) for idx_x, x in enumerate(y)] for idx_y, y in enumerate(data)]
    [[counter := counter + reset(idx_x, idx_y) for idx_x, x in enumerate(y)] for idx_y, y in enumerate(data)]
print(counter)
