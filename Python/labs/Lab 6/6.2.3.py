import random

arr = []
for i in range(20):
    arr.append(random.randint(1, 6))

name = 0
seq = dict()

for i in range(len(arr) - 1):
    if arr[i] == arr[i + 1]:
        if name not in seq:
            seq[name] = (i, i + 1)
        else:
            x, y = seq[name]
            seq[name] = (x, i + 1)
    else:
        name += 1

dist = 1
solution = []

for x, y in seq.values():
    if abs(x - y) > dist:
        dist = abs(x - y)
        solution.append((x, y))

    elif abs(x - y) == dist:
        solution.append((x, y))
    solution = [(x, y) for x, y in solution if abs(x - y) >= dist]

for i, (x, y) in enumerate(solution):
    arr.insert(x + i * 2, "(")
    arr.insert(y + 2 + i * 2, ")")

print(" ".join([str(x) for x in arr]))
