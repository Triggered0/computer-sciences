def read_file(file):
    
    try:
        if file == "input":
            file = input("Please, introduce the name of the file with the names: ")
            print()
        with open(file) as f:
            return f.read()
    except:
        print("Wrong file name")
        return read_file("input")


def check_diff(name, word):
    name = name.lower()

    diff = 0
    if len(name) != len(word):
        return 0
    else:
        for char in range(len(name)):
            if name[char] != word[char]:
                diff += 1
    return word if diff == 1 else 0


def main():

    names = read_file("input").split()
    data = read_file("parole_italiane.txt").split()

    answer = dict()
    for name in names:
        for it_name in data:
            if not name in answer:
                    answer[name] = []
            if check_diff(name, it_name) != 0:
                answer[name].append(it_name)
    for item, value in answer.items():
        print(f"Name: {item}\n{"\n".join(value) or "WARNING: No similar words were found!!!"}\n")

if __name__ == "__main__":
    main()
