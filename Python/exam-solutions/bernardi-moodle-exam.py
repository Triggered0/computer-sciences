TRIPS = "trips.txt"
STONES = "stones.txt"


def read_file(file):
    try:
        with open(file, encoding="utf-8") as f:
            return f.read()
    except OSError:
        exit("File not found")


def get_datas(visits):

    durations = []
    passengers = []
    for i in visits.split("\n"):
        name, duration, passenger = i.split(",")
        durations.append(int(duration))
        passengers.append(int(passenger))
    return (sum(durations) / len(durations), sum(passengers))


def get_common_gemstone(stones):
    stone_list = dict()
    for line in stones.split("\n"):
        for i, stone in enumerate(line.split(",")):
            if i == 0:
                continue
            stone_list[stone] = stone_list.get(stone, 0) + 1

    most = max(stone_list.items(), key=lambda x: x[1])[1]
    common = []
    for name, amount in stone_list.items():
        if most == amount:
            common.append(name)
    return common


def get_places(stones):
    locations = dict()
    for j, line in enumerate(stones.split("\n")):
        name = line.split(",")[0]
        for i, stone in enumerate(line.split(",")):
            if i == 0:
                continue
            locations[name] = locations.get(name, [])
            locations[name].append(stone)
    return locations


def main():
    trips = read_file(TRIPS)
    stones = read_file(STONES)
    duration, passenger = get_datas(trips)
    commons = get_common_gemstone(stones)
    locations = get_places(stones)
    print_locations = []
    for name, stones in locations.items():
        print_locations.append(f"* {name}: {', '.join(stones)}")
    print_locations = "\n".join(print_locations)
    print(f"""
Average duration of trips: {duration}
Total number of passengers: {passenger}
Types of gemstones by place visited:
{print_locations}
The most common types of gemstones: {', '.join(commons)}
"""
    )


if __name__ == "__main__":
    main()
