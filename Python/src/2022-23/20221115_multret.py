# Copyright © 2022 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computer-sciences
<<<<<<< HEAD
# Free for personal or classroom use; see 'LICENSE.md' for details.
=======
# Free under certain conditions — see the license for details.
>>>>>>> 89fb55792fc0bb2c474d460a143d13ae9b20111d


def main():
    _, x = foo()

    print(type(x), x)
    print(x[1])

    paola, giovanni = foo()
    print(type(paola), paola)
    print(type(giovanni), giovanni)


def foo():
    return 18, 23


if __name__ == '__main__':
    main()
