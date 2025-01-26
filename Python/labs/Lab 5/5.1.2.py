import random

numbers = []
even = []
for i in range(10):
    x = random.randint(1, 100)
    numbers.append(x)
    if x % 2:
        even.append(x)

print(
    f"Numbers: {numbers}\nEven Indexes: {numbers[::2]}\nEven Numbers: {even}\nReverse: {numbers[::-1]}\nFirst&Last: {numbers[0]}, {numbers[len(numbers)-1]}"
)
