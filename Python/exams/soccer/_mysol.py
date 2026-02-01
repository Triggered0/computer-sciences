FILE = "player_stats.csv"
teams = dict()


def get_infos(file):
    soccer = dict()
    try:
        with open(file, encoding="utf-8") as f:
            players = f.read().splitlines()
            for i, player in enumerate(players):

                if i > 0:

                    keys = players[0].split(",")
                    datas = player.split(",")

                    for i in range(len(datas)):
                        # Convert string to number only once: 1 points
                        datas[i] = int(datas[i]) if i > 2 else datas[i]

                    soccer[datas[0]] = {
                        keys[0]: datas[0],
                        keys[1]: datas[1],
                        keys[2]: datas[2],
                        keys[3]: datas[3],
                        keys[4]: datas[4],
                        keys[5]: datas[5],
                        keys[6]: datas[6],
                        keys[7]: datas[7],
                        keys[8]: datas[8],
                        keys[9]: datas[9],
                        keys[10]: datas[10],
                        keys[11]: datas[11],
                        keys[12]: datas[12],
                    }

                    teams[datas[2]] = teams.get(datas[2], {})
                    teams[datas[2]]["ages"] = teams[datas[2]].get("ages", [])
                    teams[datas[2]]["ages"].append(
                        2022 - datas[3])  # append ages

            for team in teams:
                teams[team]["average_age"] = sum(
                    teams[team]["ages"]) / len(teams[team]["ages"])

            return soccer, teams

    except OSError as e:
        exit(f"ERROR! {e}")


def calculate_effs(data):
    for key, _ in data.items():
        data[key]["forward_eff"] = (data[key]["goals"] / data[key]["minutes"]) + (
            data[key]["assists"] / data[key]["minutes"]) - (data[key]["offsides"] / data[key]["minutes"])

        teams[data[key]["team"]]["players"] = teams[data[key]
            ["team"]].get("players", [])
        teams[data[key]["team"]]["players"].append(
            (data[key]["player"], data[key]["forward_eff"]))

        k = 0 if data[key]["crosses"] == 0 else data[key]["assists"] / \
            data[key]["crosses"]  # to prevent division by 0

        data[key]["mid_eff"] = (data[key]["interceptions"] +
                                data[key]["ball_recoveries"] + k) / data[key]["minutes"]


def sort_eff_team(x):
    total = []
    for _, eff in sorted(x[1]["players"], key=lambda x: x[1], reverse=True)[:3]:
        total.append(eff)
    return sum(total)


def get_most_eff_team(data):
    sort_teams = sorted(data.items(), key=sort_eff_team, reverse=True)
    return sort_teams[0]


def main():
    players, teams = get_infos(FILE)
    calculate_effs(players)

    forward_eff_sort = sorted(
        players.items(), key=lambda x: x[1]["forward_eff"], reverse=True)
    mid_eff_sort = sorted(
        players.items(), key=lambda x: x[1]["mid_eff"], reverse=True)
    av_age_sort = sorted(teams.items(), key=lambda x: x[1]["average_age"])

    print(f"{'Name':<30}{'Team':<30}{'Forward efficiency':<30}")
    for i in range(3):
        _, value = forward_eff_sort[i]
        print(f"{value["player"]:<30}{value["team"]: < 30}{
              value["forward_eff"]: < 30.03f}")
    print()

    print(f"{'Name':<30}{'Team':<30}{'Midfield efficiency':<30}")
    for i in range(3):
        _, value = mid_eff_sort[i]
        print(f"{value["player"]:<30}{value["team"]: < 30}{
              value["mid_eff"]: < 30.03f}")
    print()

    print("The three teams with lower age average are:")
    for i in range(3):
        key, value = av_age_sort[i]
        print(f"{key:<30}{value["average_age"]:<30.02f}")
    print()

    most_eff_team = get_most_eff_team(teams)
    team_name, values = most_eff_team

    print(f"The most efficient team is {team_name}")
    for player in sorted(values["players"], key=lambda x: x[1], reverse=True)[:3]:
        name, eff = player
        print(f"{name}'s forward efficiency: {eff:.03f}")


if __name__ == "__main__":
    main()
