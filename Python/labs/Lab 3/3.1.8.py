arr = []
dupe = []

while True:
    x = input("Number: ")
    if x == "":
        break

    if x in arr:
        dupe.append(x)
    else:
        arr.append(x)

print(" ".join(dupe))
