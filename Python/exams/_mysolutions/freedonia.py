def read_file(file):
    try:
        with open(file, encoding="utf-8") as f:
            return f.read()
    except OSError as e:
        exit(f"We have a problem:\n{e}")


def get_rules():
    rules = dict()
    data = read_file("Exams/rules.dat").splitlines()
    for line in data:
        date, *lines = line.split()
        date = "".join(reversed([x.replace(":", "") for x in date.split("-")]))
        rules[date] = [x.replace("+", "").replace("-", "") for x in lines]
    return rules


def get_dates():
    data = read_file("Exams/dates.dat").splitlines()
    return ["".join(reversed(x.split("-"))) for x in data]


def main():
    rules = get_rules()
    dates = get_dates()
    print(rules, dates)
    for item, value in rules.items():
        item


if __name__ == "__main__":
    main()
