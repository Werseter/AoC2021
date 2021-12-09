def fuel_spent(pivot: int) -> int:
    return sum([((abs(x - pivot) + 1) * abs(x - pivot)) // 2 for x in data])


with open('input.txt') as fp:
    data = sorted([int(x) for x in fp.read().strip().split(',')])
low_v, high_v = fuel_spent(low := min(data)), fuel_spent(high := max(data))
while high - low > 1:
    pivot_v = fuel_spent(pivot := low + (high - low) // 2)
    if abs(pivot_v - low_v) > abs(pivot_v - high_v):
        low, low_v = pivot, pivot_v
    else:
        high, high_v = pivot, pivot_v
print(min(low_v, high_v))
