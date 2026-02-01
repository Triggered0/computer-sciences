INFO = {
    "BUDGET_goalkeeper": 20,
    "BUDGET_defender": 40,
    "BUDGET_midfielder": 80,
    "BUDGET_forward": 120,
    "goalkeeper": 3,
    "defender": 8,
    "midfielder": 8,
    "forward": 6
}


def read_file(file):
    try:
        with open(file, encoding="utf-8") as f:
            return f.read()
    except OSError as e:
        exit(f"We have an error:\n{e}")


def get_players(data):
    players = dict()
    lines = data.splitlines()
    for line in lines:
        surname, team, role, price = line.split(", ")
        players[role] = players.get(role, [])
        players[role].append((surname, team, int(price)))
    return players


def main():
    player_data = read_file("Exams/fantafoot.txt")
    players = get_players(player_data)
    for role in players:
        players[role].sort(key=lambda x: int(x[2]), reverse=True)

    for role in players:
        value = 0
        result = players[role][-(INFO[role]-2):]
        value = sum([price for (_, _, price) in result])
        for player in players[role]:
            _, _, price = player

            if value + price <= INFO[f"BUDGET_{role}"] and len(result) < INFO[role]:
                result.append(player)
                value += price

        print(f"{role.title()}: {
              " ".join([f"{name} {price}" for (name, _, price) in result])}")


if __name__ == "__main__":
    main()
