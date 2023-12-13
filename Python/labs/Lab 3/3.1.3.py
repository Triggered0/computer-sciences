x = int(input("Number: "))
y = 2

for i in range(x):
    print("*" * x)

for i in range(x * 2):
    if i > x:
        i = (i * 2 - 1) - 2 * y
        y += 2
        print(f'{"*" * (i):^100}')
    else:
        print(f'{"*" * (i * 2 - 1):^100}')
