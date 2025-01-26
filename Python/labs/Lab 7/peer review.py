INPUT_FILE = ""
OUTPUT_FILE = ""


def read_file(file):
    with open(file) as f:
        return f.read()


def write_file(file, data):
    with open(file, "w") as f:
        return f.writelines(data)


def count_words(s):
    data = s.split()
    words = dict()
    for word in data:
        word = word.lower()
        if word not in words:
            words[word] = 0
        words[word] += 1

    return sorted(words.items(), key=lambda x: x[1], reverse=True)


def main():
    data = read_file(INPUT_FILE)
    count = count_words(data)
    text = []
    for x, y in count:
        text.append(f"{x}: {y}\n")

    write_file(OUTPUT_FILE, text)


if __name__ == "__main__":
    main()
