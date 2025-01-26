def read_file(filename):
    with open(filename) as f:
        return f.read().split()


def write_file(filename, data):
    with open(filename, "w") as f:
        f.writelines(data)


def main():
    data = read_file("numbers.txt")
    values = []
    for numbers in data:
        for i in range(10):
            value = 0
            for number in numbers:
                value += int(number) ** i
            if value == int(numbers):
                values.append(numbers + "\n")
    write_file("armstrong.txt", values)


if __name__ == "__main__":
    main()
