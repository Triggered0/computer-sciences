# Copyright © 2022 Giovanni Squillero <giovanni.squillero@polito.it>
<<<<<<< HEAD
# Free for personal or classroom use; see 'LICENSE.md' for details.
# https://github.com/squillero/computer-sciences
=======
# https://github.com/squillero/computer-sciences
# Free under certain conditions — see the license for details.
>>>>>>> 89fb55792fc0bb2c474d460a143d13ae9b20111d

from string import punctuation

INPUT_FILE = 'strawberry.txt'


def main():
    words = []
    try:
        with open(INPUT_FILE) as file_in:
            for w in file_in.read().split():
                words.append(w.strip(punctuation).upper())
    except OSError:
        print(f"Yeuch, can't open \"{INPUT_FILE}\"")

    for i in range(len(words) - 2):
        if len(words[i]) == len(words[i + 1]) and len(words[i]) == len(words[i + 2]):
            print((words[i], words[i + 1], words[i + 2]))


if __name__ == '__main__':
    main()
