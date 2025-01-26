# Copyright © 2023 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computer-sciences
<<<<<<< HEAD
# Free for personal or classroom use; see 'LICENSE.md' for details.
=======
# Free under certain conditions — see the license for details.
>>>>>>> 89fb55792fc0bb2c474d460a143d13ae9b20111d


def safe_get_integer():
    value = None
    while value is None:
        try:
            string = input("Number: ")
            value = int(string)
        except ValueError as problem:
            print(problem)
            value = None
    return value


def main():
    x = safe_get_integer()
    print(x)


if __name__ == "__main__":
    main()
