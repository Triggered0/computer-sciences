import re

INPUT_FILE = "strawberry.txt"


def open_file(file):
    with open(file) as f:
        return [
            re.sub("[,.?!]", "", x.upper()) for x in f.read().split("\n") if x != ""
        ]


def write_file(file, data):
    with open(file, "w") as f:
        f.writelines(data)


def main():
    data = open_file(INPUT_FILE)
    values = []
    for el in data:
        el = el.split()
        for i in range(len(el) - 2):
            if len(el[i]) == len(el[i + 1]) and len(el[i]) == len(el[i + 2]):
                values.append(" ".join((el[i], el[i + 1], el[i + 2])) + "\n")
    write_file("strawberry_solution.txt", values)


if __name__ == "__main__":
    main()
