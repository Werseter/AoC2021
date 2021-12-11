def step(idx_x: int, idx_y: int) -> None:
    if not any(x < 0 or x >= len(data) for x in (idx_x, idx_y)) and data[idx_y][idx_x] != -1:
        data[idx_y][idx_x] += 1


def burst(idx_x: int, idx_y: int) -> None:
    if data[idx_y][idx_x] > 9:
        data[idx_y][idx_x] = -1
        for x_shift in range(-1, 2):
            for y_shift in range(-1, 2):
                step(idx_x + x_shift, idx_y + y_shift)


def reset(step_idx: int) -> int | None:
    step_counter = 0
    for idx_y, y in enumerate(data):
        for idx_x in range(len(data)):
            if data[idx_y][idx_x] == -1:
                data[idx_y][idx_x] = 0
                step_counter += 1
    if step_counter == 100:
        return step_idx


with open('input.txt') as fp:
    data = [[int(y) for y in x.strip()] for x in fp.readlines()]
step_idx = 0
while True:
    [[step(idx_x, idx_y) for idx_x, x in enumerate(y)] for idx_y, y in enumerate(data)]
    while [elem for row in data for elem in row if elem > 9]:
        [[burst(idx_x, idx_y) for idx_x, x in enumerate(y)] for idx_y, y in enumerate(data)]
    if result := reset(step_idx := step_idx + 1):
        print(result)
        break
