# Copyright © 2022 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computer-sciences
<<<<<<< HEAD
# Free for personal or classroom use; see 'LICENSE.md' for details.
=======
# Free under certain conditions — see the license for details.
>>>>>>> 89fb55792fc0bb2c474d460a143d13ae9b20111d

FILENAME1 = 'file1.txt'
FILENAME2 = 'file2.txt'


def main():
    with open(FILENAME1) as f1, open(FILENAME2, 'w') as f2:
        for line in reversed(f1.readlines()):
            f2.write(line)


if __name__ == '__main__':
    main()
