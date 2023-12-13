def merge(a, b):
    arr = []
    for i in range(max(len(a), len(b))):
        try:
            arr.append(a[i])
            arr.append(b[i])
        except:
            arr.append(b[i])
    return arr


x = merge([1, 2, 3, 4, 5], [9, 8, 7, 6, 5, 3, 3, 3, 3])
print(x) 