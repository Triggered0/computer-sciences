def read_file(file):
    try:
        with open(file, "r") as f:
            return f.read()
    except OSError as e:
        exit(f"Error reading file: {e}")


def write_file(file, content):
    try:
        with open(file, "w") as f:
            return f.write(content)
    except OSError as e:
        exit(f"Error writing file: {e}")


def main():
    data = read_file("Exams/numbers.txt")
    lines = data.split("\n")
    solution = list()

    for number in lines:
        integers = list(number)
        for i in range(10):
            value = 0
            for armnum in integers:
                value += int(armnum) ** i

            if value == int(number):
                solution.append(str(value))

    text = "\n".join(solution)

    write_file("armstrong.txt", text)


if __name__ == "__main__":
    main()
