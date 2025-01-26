map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
skip = []


def roman_to_decimal(str):
    total = 0

    slist = list(str)

    for i in range(len(slist)):
        slist[i] = map[slist[i]]

    for i in range(len(slist)):
        if i < len(slist) - 1 and slist[i] < slist[i + 1]:
            total -= slist[i]
        else:
            total += slist[i]

    return total

print(roman_to_decimal("MCMLXXVIII"))