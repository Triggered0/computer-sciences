def read_file(file):
    try:
        with open(file) as f:
            words = []
            murat = f.read()

            for string in murat.split():
                words.append(string.strip('.,"'))

            return words

    except OSError as e:
        exit(f"we have an error:\n{e}")


def main():
    words = read_file("strawberry.txt")

    for i in range(len(words) - 2):

        if len(words[i]) == len(words[i+1]) == len(words[i+2]):
            print((words[i].upper(), words[i+1].upper(), words[i+2].upper()))


if __name__ == "__main__":
    main()
