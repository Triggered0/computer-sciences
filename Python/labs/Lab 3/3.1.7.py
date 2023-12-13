x = input("String: ")

for i in range(1, len(x)):
    for j in range(1, len(x) + 2 - i):
        print(x[j - 1 : j - 1 + i])
print(x)
