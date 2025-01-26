# Copyright © 2022 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computer-sciences
<<<<<<< HEAD
# Free for personal or classroom use; see 'LICENSE.md' for details.
=======
# Free under certain conditions — see the license for details.
>>>>>>> 89fb55792fc0bb2c474d460a143d13ae9b20111d


def main():
    # lists contains generic objects, thus a list may contain lists

    birthdays = [[23, 10, 'Giovanni'], [18, 5, 'Paola']]

    for b in birthdays:
        print(f"{b[0]}-{b[1]} -> {b[2]}")

    for i in range(len(birthdays)):  # Terrible!
        print(birthdays[i])

    for i, b in enumerate(birthdays):  # Correct ;-)
        print(f"{i}: {b[0]}-{b[1]} -> {b[2]}")

    print(birthdays)


if __name__ == '__main__':
    main()
