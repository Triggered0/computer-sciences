import random

numbers = []

for i in range(10):
    x = random.randint(1, 100)
    numbers.append(x)

print(numbers)


def remove_min(x):
    last = max(x)
    for i in range(len(x)):
        if x[i] < last:
            last = x[i]
    x.pop(x.index(last))
    print(last)
    return x


print(remove_min(numbers))
