import re

str = input("String: ")
arr = list(str)
print("".join([*reversed(arr)]))
print("".join([*reversed(re.findall("[A-Z]", str))]))
