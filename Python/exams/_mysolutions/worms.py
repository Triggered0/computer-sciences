FILE = "seq.txt"


def read_file():
    try:
        with open(FILE) as f:
            return f.read()
    except OSError:
        exit("file error")


def find_distance(text, word1, word2):
    print(text)
    w1d = []
    w2d = []
    for i, word in enumerate(text.split()):
        if word == word1:
            w1d.append(i)
        elif word == word2:
            w2d.append(i)
    return w1d, w2d


def find_closest(list1, list2):
    distance = 100
    if len(list1) > 0 and len(list2) > 0:
        for i in range(len(list1)):
            for x in range(len(list2)):
                if abs(list1[i] - list2[x]) < distance:
                    distance = abs(list1[i] - list2[x])
                return distance


def main():
    word1 = input("First word to look for: ")
    word2 = input("Second word to look for: ")
    data = read_file().split("\n")

    total = 0
    for i in range(len(data)):
        if word1 in data[i] and word2 in data[i]:
            total += 1
        x, y = find_distance(data[i], word1, word2)
        if total == 0:
            print("The two words never appear in the same sequence")
        else:
            if find_closest(x, y) == None:
                "sa"


if __name__ == "__main__":
    main()
