x = input("Enter a number sequence: ").split()
total = int(x[0])

for i in range(1, len(x)):
    x[i] = int(x[i])
    if i % 2 == 0:
        total -= x[i]
    else:
        total += x[i]
print(total)
