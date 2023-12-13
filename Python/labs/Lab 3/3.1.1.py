even = 0
odd = 0
numbers = []

while True:
    sum = 0
    x = input("Number: ")

    if x == "":
        break

    numbers.append(x)
    x = int(x)

    if x % 2 == 0:
        even += 1

    else:
        odd += 1

    for i in numbers:
        sum += int(i)

    if len(numbers) == 1:
        print(numbers[0])

    else:
        print(f'{" + ".join(numbers)} = {sum}')
        print(f"Odd: {odd} - Even: {even}")
