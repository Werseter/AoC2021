with open('input.txt') as fp:
    dot_data, _, fold_data = fp.read().strip().partition('\n\n')
board: set[tuple[int, int]] = set()
for dot in dot_data.splitlines():
    tmp1, _, tmp2 = dot.partition(',')
    board.add((int(tmp1), int(tmp2)))
for fold in fold_data.splitlines():
    tmp1, _, tmp2 = fold.partition('=')
    fold_side, fold_line = tmp1[-1], int(tmp2)
    for x, y in board.copy():
        if fold_side == 'y' and y > fold_line:
            board.remove((x, y))
            board.add((x, y - 2 * (y - fold_line)))
        elif fold_side == 'x' and x > fold_line:
            board.remove((x, y))
            board.add((x - 2 * (x - fold_line), y))
ret = ''
for y in range(max(y for x, y in board) + 1):
    for x in range(max(x for x, y in board) + 1):
        ret += '#' if (x, y) in board else ' '
    ret += '\n'
print(ret)
