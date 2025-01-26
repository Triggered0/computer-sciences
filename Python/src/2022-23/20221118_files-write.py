# Copyright © 2022 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computer-sciences
<<<<<<< HEAD
# Free for personal or classroom use; see 'LICENSE.md' for details.
=======
# Free under certain conditions — see the license for details.
>>>>>>> 89fb55792fc0bb2c474d460a143d13ae9b20111d

FILENAME = 'test.dat'


def main():
    with open(FILENAME, "w") as my_file:
        my_file.write("Hello! This is my first file.\n")
        my_file.write("Hello! This is my first file.\n")


if __name__ == '__main__':
    main()
