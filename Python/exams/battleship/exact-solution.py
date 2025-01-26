MOVES_FILE = "moves.txt"
ROW_INDEX = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4,
             "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}


def get_maps():
    try:
        cords = []
        maps = input(
            "names of the files that contain ship positions (write the names seperated with comma):\n ").split(",")

        for map in maps:
            with open(map, encoding="utf-8") as f:
                lines = f.read().splitlines()
                map_list = []

                for line in lines:
                    chars = list(line)
                    map_list.append(chars)
                cords.append(map_list)

        return cords

    except OSError as e:
        exit(f"ERROR! {e}")


def get_moves(file):
    moves = []
    try:
        with open(file) as f:
            content = f.read()
            lines = content.splitlines()
            for line in lines:
                row, col = line.split(",")
                moves.append((row, int(col) - 1))
            return moves
    except OSError as e:
        exit(f"ERROR! {e}")


def check_win(winner_map):
    win = 0
    for row in winner_map:

        if "#" in row:
            win += 1

    if win == 0:
        return "win"

    return "continue"


def list_to_string(player_map):
    rows = []

    for row in player_map:
        full_row = "".join(row)
        rows.append(full_row)

    full = "\n".join(rows)
    return full


def main():
    map1, map2 = get_maps()
    moves = get_moves(MOVES_FILE)
    any_winner = 0

    for i, move in enumerate(moves):

        row, col = move

        if i % 2 == 0:
            player = 2
            player_map = map1
        else:
            player = 1
            player_map = map2

        print(f"PLAYER {player}")
        print(f"({row}, {col + 1})")

        if player_map[ROW_INDEX[row]][col] == "#":
            player_map[ROW_INDEX[row]][col] = "*"
            print("HIT")
        else:
            player_map[ROW_INDEX[row]][col] = "o"
            print("MISS")
        print()

        if check_win(player_map) == "win":
            print(f"PLAYER {player} WINS\n\n")
            print(f"PLAYER 1'S MAP\n{list_to_string(map1)}\n")
            print(f"PLAYER 2'S MAP\n{list_to_string(map2)}")
            any_winner = 1
            break

    if any_winner == 0:
        print("NO WINNER - DRAW")


if __name__ == "__main__":
    main()
