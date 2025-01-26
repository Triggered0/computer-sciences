# Copyright © 2022 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computer-sciences
<<<<<<< HEAD
# Free for personal or classroom use; see 'LICENSE.md' for details.
=======
# Free under certain conditions — see the license for details.
>>>>>>> 89fb55792fc0bb2c474d460a143d13ae9b20111d

from pprint import pprint

DIMX = 20
DIMY = 4


def main():
    table = list()
    for x in range(DIMY):
        table.append([0] * DIMX)
    table[2][3] = 6
    pprint(table)


if __name__ == '__main__':
    main()
