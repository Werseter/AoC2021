import operator
from collections.abc import Collection, Sequence
from itertools import islice
from typing import Callable


def get_nth_mcb(data: Collection[str], idx: int) -> str:
    return str(int(int(''.join(next(islice(zip(*data), idx, None))), 2).bit_count() >= len(data) / 2))


def filter_data(data: Sequence[str], comparison: Callable[[str, str], bool]) -> int:
    idx = 1
    while len(data) > 1:
        data = [x for x in data if comparison(x[idx], get_nth_mcb(data, idx))]
        idx += 1
    return int(data[0], 2)


with open('input.txt') as fp:
    data = [x.strip() for x in fp.readlines()]

oxygen_data: list[str] = []
co2_data: list[str] = []
mcb = get_nth_mcb(data, 0)
for x in data:
    (oxygen_data if mcb == x[0] else co2_data).append(x)

oxygen_rating = filter_data(oxygen_data, operator.eq)
co2_rating = filter_data(co2_data, operator.ne)
print(oxygen_rating * co2_rating)
