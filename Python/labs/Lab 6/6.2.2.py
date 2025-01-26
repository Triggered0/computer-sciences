arr = [1, 2, 3, 4, 5]
arr.insert(0, arr[len(arr) - 1])
arr.pop()
print(arr)
