from collections import deque

with open('input.txt') as fp:
    data = [int(x) for x in fp.read().strip().split(',')]
    fish_timers = deque({**{x: 0 for x in range(9)}, **{x: data.count(x) for x in set(data)}}.values())
for _ in range(80):
    fish_timers.rotate(-1)
    fish_timers[6] += fish_timers[-1]
print(sum(fish_timers))
