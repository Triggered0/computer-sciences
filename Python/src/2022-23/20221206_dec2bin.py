# Copyright © 2022 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computer-sciences
<<<<<<< HEAD
# Free for personal or classroom use; see 'LICENSE.md' for details.
=======
# Free under certain conditions — see the license for details.
>>>>>>> 89fb55792fc0bb2c474d460a143d13ae9b20111d


def dec2bin(num):
    mods = list()
    while num > 0:
        mods.append(num % 2)
        num = num // 2
    if not mods:
        result = '0'
    else:
        result = ''
        for d in reversed(mods):
            result += str(d)
    return result


def main():
    try:
        number = int(input("Number: "))
    except ValueError as error:
        print(f"Yeuch! {error}")
        exit(1)
    binary = dec2bin(number)
    print(f"{number}|10 -> {binary}|2")


if __name__ == '__main__':
    main()
