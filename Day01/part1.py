with open('input.txt') as fp:
    data = (int(x) for x in fp.readlines())
it = iter(data)
a = next(it)
counter = 0
while (b := next(it, None)) is not None:
    if b > a:
        counter += 1
    a = b
print(counter)
