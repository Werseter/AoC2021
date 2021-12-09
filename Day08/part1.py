with open('input.txt') as fp:
    data = [x.partition('|')[-1].strip().split() for x in fp.readlines()]
print(len([x for x in (len(item) for sublist in data for item in sublist) if x in (2, 3, 4, 7)]))
