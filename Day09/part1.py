def is_local_min(x: int, idx_x: int, idx_y: int):
    a = data[idx_y - 1][idx_x] if idx_y > 0 else 10
    b = data[idx_y + 1][idx_x] if idx_y < len(data) - 1 else 10
    c = data[idx_y][idx_x - 1] if idx_x > 0 else 10
    d = data[idx_y][idx_x + 1] if idx_x < len(data[0]) - 1 else 10
    return x + 1 if all(x < y for y in (a, b, c, d)) else 0


with open('input.txt') as fp:
    data = [[int(y) for y in x.strip()] for x in fp.readlines()]
risk_matrix = [[is_local_min(x, idx_x, idx_y) for idx_x, x in enumerate(y)] for idx_y, y in enumerate(data)]
print(sum((elem for row in risk_matrix for elem in row)))
