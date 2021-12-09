from scipy.optimize import minimize


def fuel_spent(pivot: int) -> int:
    return sum([((abs(x - pivot) + 1) * abs(x - pivot)) // 2 for x in data])


with open('input.txt') as fp:
    data = sorted([int(x) for x in fp.read().strip().split(',')])
print(fuel_spent(round(minimize(fuel_spent, x0=data[len(data) // 2], tol=0.5,  method='Powell').x[0])))
