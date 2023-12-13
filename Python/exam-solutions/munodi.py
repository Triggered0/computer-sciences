FILE = "Exams/seq.txt"


def read_file():
    try:
        with open(FILE) as f:
            return f.read()
    except OSError:
        exit("File does not exists")


def main():
    data = read_file().split("\n")

    for index, line in enumerate(data):
        line = line.split()
        line = [int(x) for x in line]
        isMunodi = False

        for i in range(len(line) - 1):
            if line[i] % 2 == 0:
                if line[i] / 2 != line[i + 1]:
                    print(f"Sequence {index + 1} is NOT a Munodi sequence")
                    isMunodi = True
                    break
            else:
                if (3 * line[i]) + 1 != line[i + 1]:
                    print(f"Sequence {index + 1} is NOT a Munodi sequence")
                    isMunodi = True
                    break

        if not isMunodi:
            print(f"Sequence {index+1} is a Munodi sequence (length {len(line)})")


if __name__ == "__main__":
    main()
