INPUT_FILE = "indices.txt"
OUTPUT_FILE = "indices_strips.txt"


def read_file():
    try:
        with open(INPUT_FILE) as f:
            return f.read()
    except OSError:
        exit("File not found")


def write_file(file, data):
    with open(file, "w") as f:
        return f.write(data)


def main():
    data = read_file().split("\n")
    solution = []

    for i in range(len(data) - 1):
        line = data[i].split()
        nextline = data[i + 1].split()

        if line[1] == nextline[0] and line[2] == nextline[1]:
            solution.append(line[0])
        else:
            exit("Indices do not match")

        if i == len(data) - 2:
            solution.extend((line[1], line[2], nextline[2]))

    write_file(OUTPUT_FILE, " ".join(solution))


if __name__ == "__main__":
    main()
