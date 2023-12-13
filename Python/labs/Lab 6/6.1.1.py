def read_file(file):
    with open(file) as f:
        return f.read()


def write_file(file, data):
    with open(file, "w") as f:
        return f.writelines(data)


def main():
    data = read_file("input.txt")
    stn = []

    for i, line in enumerate(data.split("\n")):
        stn.append(f"/*{i+1}*/{line}\n")
    write_file("output.txt", stn)


if __name__ == "__main__":
    main()
