# Copyright © 2022 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computer-sciences
<<<<<<< HEAD
# Free for personal or classroom use; see 'LICENSE.md' for details.
=======
# Free under certain conditions — see the license for details.
>>>>>>> 89fb55792fc0bb2c474d460a143d13ae9b20111d


def main():
    x = list()
    x.append(23)
    x.append(10)
    x.append('Giovanni')
    foo(x)
    # the object bound to 'x' has changed
    print(x)


def foo(y):
    # the object bound to 'y' does change
    y.append(18)
    y.append(5)
    y.append('Paola')


if __name__ == '__main__':
    main()
