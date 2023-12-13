numbers = []
maximas = []
while True:
    x = input("Enter a number: ")
    if x == "":
        break
    else:
        numbers.append(int(x))

print(numbers)

for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
        maximas.append((numbers[i], i))
    if len(maximas) == 0:
        maximas = "There are no local maxima"

print(maximas[:2:])
