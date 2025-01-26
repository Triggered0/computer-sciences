# Copyright © 2022 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computer-sciences
<<<<<<< HEAD
# Free for personal or classroom use; see 'LICENSE.md' for details.
=======
# Free under certain conditions — see the license for details.
>>>>>>> 89fb55792fc0bb2c474d460a143d13ae9b20111d

FILENAME = 'song.txt'


def main():
    my_file = open(FILENAME)
    x = my_file.read()
    print(x)
    my_file.close()


if __name__ == '__main__':
    main()
