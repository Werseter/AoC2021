with open('input.txt') as fp:
    data = sorted(int(x) for x in fp.read().strip().split(','))
    tmp = data[len(data) // 2]
    print(sum(abs(x - tmp) for x in data))
