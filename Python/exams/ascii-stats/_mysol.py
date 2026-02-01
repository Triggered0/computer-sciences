FILE = "landscape.txt"


def read_file(filename):
    try:
        with open(filename) as f:
            return f.read()
    except OSError as e:
        exit(f"ERROR! {e}")


def get_inputs():
    try:
        xy = input("Please, enter the coordinates (x,y): ")
        square = input("Please, enter the square size: ")
        return [int(x) for x in xy.split(",")], int(square)
    except:
        print("Wrong Input")
        return get_inputs()


def main():
    data = read_file(FILE)
    splitted_data = data.split()
    xy, square = get_inputs()
    rows = len(data.split())
    columns = len(data.split()[0])

    if (
        xy[0] > rows
        or xy[0] + square > rows
        or xy[1] > columns
        or xy[1] + square > columns
    ):
        print("ERROR!! The square to analyze is out of limits.")
        return main()

    img = dict()
    for i, row in enumerate(splitted_data):
        if i >= xy[1] and i < xy[1] + square:
            for x, char in enumerate(row):
                if x >= xy[0] and x < xy[0] + square:
                    img[char] = img.get(char, 0) + 1

    for s in sorted(img, key=lambda k: img[k], reverse=True):
        print(f"{s} -> {(img[s] / square ** 2) * 100:.1f}%")


if __name__ == "__main__":
    main()
