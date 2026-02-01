FILE = "Exams/actions.txt"


def read_file():
    try:
        with open(FILE) as f:
            actions = []
            for line in f.read().split("\n"):
                actions.append((0 if "takes" in line else 1, line.split()[3]))
            return actions

    except OSError:
        exit("File does not exists")


def main():
    actions = read_file()

    for action, item in actions:
        action


if __name__ == "__main__":
    main()
