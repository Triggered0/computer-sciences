# Copyright © 2022 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computer-sciences
<<<<<<< HEAD
# Free for personal or classroom use; see 'LICENSE.md' for details.
=======
# Free under certain conditions — see the license for details.
>>>>>>> 89fb55792fc0bb2c474d460a143d13ae9b20111d


def bin2dec(binary):
    num = 0
    for d in binary:
        num = num * 2 + int(d)
    return num


def main():
    binary = input()
    print(bin2dec(binary))


if __name__ == '__main__':
    main()
