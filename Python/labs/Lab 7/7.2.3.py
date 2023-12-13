import re


def read_file(file):
    with open(file) as f:
        return f.read().split("\t")


def main():
    data = read_file("rawdata_2004.txt")
    x = list(filter(bool, data))

    countries = dict()

    for i in range(len(x) - 1):
        if i % 2 == 1:
            countries[x[i]] = re.sub("(\$ +|\\n\d+)", "", x[i + 1]).replace("\n", "")

    print(countries)


if __name__ == "__main__":
    main()
