def read_file(file):
    try:
        with open(file, encoding="utf-8") as f:
            return f.read()
    except OSError as e:
        exit(f"ERROR! {e}")


def get_mosts(data):

    most10 = max(data, key=lambda x: x[1]["scores"].count("10"))
    most0 = max(data, key=lambda x: x[1]["scores"].count("0"))

    if most10[1]["scores"].count("10") == 0:
        most10 = None
    if most0[1]["scores"].count("0") == 0:
        most0 = None

    return most10, most0


def main():
    data = read_file("Exams/bowling/bowling.txt")
    lines = data.splitlines()
    bowling = dict()

    for line in lines:
        surname, name, *scores = line.split(";")
        bowling[f"{surname} {name}"] = {"scores": [], "sum": 0}
        bowling[f"{surname} {name}"]["sum"] = sum([int(x) for x in scores])
        bowling[f"{surname} {name}"]["scores"] = scores

    bowling = sorted(bowling.items(), key=lambda x: x[1]["sum"], reverse=True)
    most10, most0 = get_mosts(bowling)

    for key, value in bowling:
        print(f"{key} {value["sum"]}")

    if not most10:
        print("No player scored 10")
    else:
        print(f"Most 10: {most10[0]} ({most10[1]["scores"].count("10")} {
              "times" if most10[1]["scores"].count("10") > 1 else "time"})")

    if not most0:
        print("No player scored 0")
    else:
        print(f"Most 0: {most0[0]} ({most0[1]["scores"].count("0")} {
              "times" if most0[1]["scores"].count("0") > 1 else "time"})")


if __name__ == "__main__":
    main()
