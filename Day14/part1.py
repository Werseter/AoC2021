with open('input.txt') as fp:
    polymer_data, _ = list(fp.readline().strip()), fp.readline()
    insertion_data = dict(x.strip().partition(' -> ')[::2] for x in fp.readlines())
for step_idx in range(10):
    for idx, (a, b) in enumerate(zip(polymer_data[:-1], polymer_data[1:]), 1):
        polymer_data.insert(2 * idx - 1, insertion_data[a + b])
polymer_counts = sorted([polymer_data.count(x) for x in set(polymer_data)])
print(polymer_counts[-1] - polymer_counts[0])
