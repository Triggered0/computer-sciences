from pprint import pprint
INPUT_FILE = 'Exams/fantafoot.txt'


def create_roles_dict(filename):
    player_dict = dict()
    with open(filename, 'r', encoding='utf-8') as infile:
        for line in infile:
            name, _, role, money = line.strip().split(", ")
            player_dict[name] = (role, money)
    return dict(sorted(player_dict.items(), key=lambda t: int(t[1][1]), reverse=True))


def buy(data):
    mid = 8
    forward = 6
    defender = 8
    goal = 3
    goal_budget = 0
    defender_budget = 0
    mid_budget = 0
    forward_budget = 0
    goal_keeper = list()
    forwards = list()
    mids = list()
    defenders = list()

    for name, features in data.items():
        if features[0] == "goalkeeper" and 0 < goal <= 3 and goal_budget+int(features[1])+goal-1 <= 20:
            goal_keeper.append((name, features[1]))
            goal_budget += int(features[1])
            goal -= 1
        if features[0] == "defender" and 0 < defender <= 8 and defender_budget+int(features[1])+defender-1 <= 40:
            defenders.append((name, features[1]))
            defender_budget += int(features[1])
            defender -= 1
        if features[0] == "midfielder" and 0 < goal <= 8 and mid_budget+int(features[1])+mid-1 <= 80:
            mids.append((name, features[1]))
            mid_budget += int(features[1])
            mid -= 1
        if features[0] == "forward" and 0 < forward <= 6 and forward_budget+int(features[1])+forward-1 <= 120:
            forwards.append((name, features[1]))
            forward_budget += int(features[1])
            forward -= 1
    return goal_keeper, defenders, mids, forwards


def main():
    player_dict = create_roles_dict(INPUT_FILE)
    # print(player_dict)
    goal, defend, mid, forward = buy(player_dict)
    print(f"""Goal keepers : {goal}
Defenders {defend}
Midfielders {mid}
Forwards {forward}""")


if __name__ == '__main__':
    main()
