FILE_NAME = "plotter.txt"


def create_table(n):
    table = []
    for _ in range(n):
        table.append(["."] * n)
    return table


def print_table(table):
    for line in table:
        print("".join(line))


def get_plotters(file):
    plots = []
    try:
        with open(file, encoding="utf-8") as f:
            lines = f.read().splitlines()
            for line in lines:
                plots.append(line.split())
        return plots
    except OSError as err:
        exit(f"ERROR! {err}")


def main():
    table = create_table(5)
    data = get_plotters(FILE_NAME)

    for line in data:
        char, *cords = line
        cords = [int(x) for x in cords]
        table_length = len(table) - 1

        if char == "P":
            table[table_length - cords[0]][cords[1]] = "*"

        if char == "H":
            x, y, l = cords
            line = table[table_length - y]

            for i in range(l):
                line[x + i] = "+" if line[x + i] == "|" else line[x + i] = "-"

        if char == "V":
            x, y, l = cords

            for i in range(l):
                table[table_length - y - i][x] = "+" if table[table_length - y - i][x] == "-" else table[table_length - y - i][x] = "|"

    print_table(table)


if __name__ == "__main__":
    main()
