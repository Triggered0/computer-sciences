def read_file(file):
    with open(file) as f:
        return f.read()


def write_file(file, data):
    with open(file, "w") as f:
        return f.writelines(data)


def main():
    data = read_file("input.txt")
    write_file("output.txt", [x + "\n" for x in data.split("\n")[::-1]])


if __name__ == "__main__":
    main()
