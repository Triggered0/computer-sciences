def read_file(file):
    with open(file) as f:
        return f.read()


def write_file(file, data):
    with open(file, "w") as f:
        return f.writelines(data)


def main():
    try:
        inp = input("File names: ")
        word = input("Word to search for: ")
        data = inp.split(",")
        if len(data) != 3:
            exit("Wrong input")
    except:
        exit("Wrong input")

    for file in data:
        try:
            file_data = read_file(file)
            for line in file_data.split("\n"):
                if word.lower() in line.lower():
                    print(f"{file}: {line}")
        except:
            exit("Couldn't find the file")


if __name__ == "__main__":
    main()