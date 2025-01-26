from pprint import pprint


def main():
    row = input("Row count: ")
    column = input("Column count: ")

    table = []

    try:
        row = int(row)
        column = int(column)
    except ValueError as e:
        exit(f"Error in int func: {e}")

    for i in range(column):
        arr = []
        for i in range(row):
            arr.append(0)
        table.append(arr)
    print("Step I.")
    pprint(table)
    print()

    for x in table:
        for i in range(len(x)):
            x[i] = 1
    print("Step II.")
    pprint(table)
    print()

    for index, x in enumerate(table):
        for i in range(len(x)):
            if index % 2 == 0:
                x[i] = 1 if i % 2 == 0 else 0
            else:
                x[i] = 0 if i % 2 == 0 else 1
    print("Step III.")
    pprint(table)
    print()

    for index, x in enumerate(table):
        for i in range(len(x)):
            if index == 0:
                x[i] = 1
            elif index == len(x) - 1:
                x[i] = 1
            else:
                x[i] = 0
    print("Step IV.")
    pprint(table)
    print()

    for index, x in enumerate(table):
        for i in range(len(x)):
            if i == 0:
                x[i] = 1
            elif i == len(x) - 1:
                x[i] = 1
            else:
                x[i] = 0
    print("Step V.")
    pprint(table)
    print()

    total = 0
    for index, x in enumerate(table):
        total += sum(x)

    print("Step VI.")
    print(total)


if __name__ == "__main__":
    main()
