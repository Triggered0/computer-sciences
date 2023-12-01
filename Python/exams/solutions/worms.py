FILE = "Exams/seq.txt"


def read_file():
    try:
        with open(FILE) as f:
            return f.read()
    except OSError as e:
        exit("File does not exists" + e)


def main():
    word1 = input("First word: ")
    word2 = input("Second word: ")
    list1 = []
    list2 = []

    data = read_file().split("\n")

    for index, line in enumerate(data):
        if word1 in line and word2 in line:
            found = index
            break
        else:
            found = False

    if not found:
        print("The two words never appear in the same sequence")
    else:
        for index, word in enumerate(data[found].split()):
            if word == word1:
                list1.append(index)
            elif word == word2:
                list2.append(index)
        distance = find_closest(list1, list2)
        print(f"Min distance: sequence {found+1} ({distance=})")


def find_closest(list1, list2):
    distance = 100
    for i in range(len(list1)):
        for j in range(len(list2)):
            if abs(list1[i] - list2[j]) < distance:
                distance = abs(list1[i] - list2[j])
    return distance


if __name__ == "__main__":
    main()
