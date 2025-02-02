# Copyright © 2022 Giovanni Squillero <squillero@polito.it>
# https://github.com/squillero/computer-sciences
<<<<<<< HEAD
# Free for personal or classroom use; see 'LICENSE.md' for details.
=======
# Free under certain conditions — see the license for details.
>>>>>>> 89fb55792fc0bb2c474d460a143d13ae9b20111d

FILENAME_A = 'file-a.dat'
FILENAME_B = 'file-b.dat'


def read_file(filename):
    data = list()
    try:
        with open(filename, encoding='utf-8') as file_in:
            data = list(file_in)
    except OSError as problem:
        print(f"Problem with \"{filename}\": {problem}")
    return data


def main():
    file_a = read_file(FILENAME_A)
    file_b = read_file(FILENAME_B)
    data = dict()
    for lang, greet in zip(file_a, file_b):
        data[lang.strip()] = greet.strip()
    for lang, greet in data.items():
        print(f"In {lang} we say \"{greet}\"")


if __name__ == '__main__':
    main()
