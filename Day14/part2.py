from collections import defaultdict

polymer_count: defaultdict[str, int] = defaultdict(int)
pair_count: defaultdict[str, int] = defaultdict(int)

with open('input.txt') as fp:
    polymer_data, _ = list(fp.readline().strip()), fp.readline()
    insertion_data = dict(x.strip().partition(' -> ')[::2] for x in fp.readlines())
for polymer in polymer_data:
    polymer_count[polymer] += 1
for a, b in zip(polymer_data[:-1], polymer_data[1:]):
    pair_count[a + b] += 1
for step_idx in range(40):
    pair_count_processing_copy = {pair: count for pair, count in pair_count.items() if count}
    for (a, b) in pair_count_processing_copy:
        polymer_count[insertion_data[a + b]] += pair_count_processing_copy[a + b]
        pair_count[a + insertion_data[a + b]] += pair_count_processing_copy[a + b]
        pair_count[insertion_data[a + b] + b] += pair_count_processing_copy[a + b]
        pair_count[a + b] -= pair_count_processing_copy[a + b]
polymer_counts = sorted(polymer_count.values())
print(polymer_counts[-1] - polymer_counts[0])
