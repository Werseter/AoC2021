from itertools import islice

with open('input.txt') as fp:
    data = (int(x) for x in fp.readlines())
it = iter(data)
a, b, c = islice(it, 3)
counter = 0
while (d := next(it, None)) is not None:
    if d > a:
        counter += 1
    a, b, c = b, c, d
print(counter)
