from pprint import pprint


def main():
    m = 8
    n = 10
    row, column = m, n
    table = []

    for i in range(row):
        arr = []
        for j in range(column):
            arr.append(0)
        table.append(arr)
    print("Step I.")
    pprint(table)
    print()

    for i in range(row):
        for j in range(column):
            table[i][j] = 1
    print("Step II.")
    pprint(table)
    print()

    for i in range(row):
        for j in range(column):
            if i % 2 == 0:
                table[i][j] = 1 if j % 2 == 0 else 0
            else:
                table[i][j] = 0 if j % 2 == 0 else 1
    print("Step III.")
    pprint(table)
    print()

    for i in range(row):
        for j in range(column):
            if i == 0:
                table[i][j] = 0
            elif i == row - 1:
                table[i][j] = 0
    print("Step IV.")
    pprint(table)
    print()

    for i in range(row):
        for j in range(column):
            if j == 0:
                table[i][j] = 1
            elif j == column - 1:
                table[i][j] = 1
    print("Step V.")
    pprint(table)
    print()

    print("Step VI.")
    print(sum([item for row in table for item in row]))


if __name__ == "__main__":
    main()
