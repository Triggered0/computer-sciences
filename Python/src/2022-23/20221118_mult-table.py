# Copyright © 2022 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computer-sciences
<<<<<<< HEAD
# Free for personal or classroom use; see 'LICENSE.md' for details.
=======
# Free under certain conditions — see the license for details.
>>>>>>> 89fb55792fc0bb2c474d460a143d13ae9b20111d

from pprint import pprint

DIM = 10


def make_table(dim):
    table = list()
    for r in range(dim):
        table.append([0] * dim)
    return table


def print_table(table):
    for row in table:
        for element in row:
            print(f"{element:4d}", end='')
        print()


def main():
    table = make_table(DIM)
    for x in range(DIM):
        for y in range(DIM):
            table[x][y] = (x + 1) * (y + 1)
    #pprint((table))
    print_table(table)


if __name__ == '__main__':
    main()
