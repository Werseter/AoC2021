with open('input.txt') as fp:
    data = [x.strip() for x in fp.readlines()]
half_data_len = len(data) / 2
tmp = (int(''.join(x), 2) for x in zip(*data))
mcb = [int(x.bit_count() >= half_data_len) for x in tmp]
lcb = (int(not x) for x in mcb)
gamma = int(''.join(str(x) for x in mcb), 2)
epsilon = int(''.join(str(x) for x in lcb), 2)
print(gamma * epsilon)
