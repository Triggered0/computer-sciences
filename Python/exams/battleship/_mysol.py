MOVES_FILE = "moves.txt"
ROWS = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4,
        "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}


def get_ship_cords():
    try:
        file_names = input(
            "name of the files that contains ship positions (write the file names separated with comma): ").split(",")
        cords = []
        for file in file_names:
            with open(file) as f:
                lines = []
                for line in f.read().splitlines():
                    lines.append(list(line))
                cords.append(lines)
        return cords
    except OSError as e:
        exit(f"ERROR! {e}")


def get_moves(file):
    moves = []
    try:
        with open(file) as f:
            for line in f.read().splitlines():
                row, column = line.split(",")
                moves.append((row, int(column)-1))
        return moves
    except OSError as e:
        exit(f"ERROR! {e}")


def check_win(player):
    if not "#" in arr_to_str(player):
        return "win"
    return "continue"


def arr_to_str(data):
    arr = "\n".join(["".join(x) for x in data])
    return arr


def main():
    map0, map1 = get_ship_cords()
    moves = get_moves(MOVES_FILE)
    game_result = ""

    for i, (row, col) in enumerate(moves):
        icol = ROWS[row]

        if i % 2 == 0:
            map = map0
            player = 1
        else:
            map = map1
            player = 0

        print(f"PLAYER [{player}]'s Turn ({row}, {col+1})")

        if map[icol][col] == "#":
            map[icol][col] = "*"
            print(f"PLAYER [{player}] - hit")
        else:
            map[icol][col] = "o"
            print(f"PLAYER [{player}] - miss")

        print(arr_to_str(map).replace("#", "-"))
        print()

        if check_win(map) == "win":
            game_result = "ended"
            print(f"GAME OVER! PLAYER [{player}] - WINS\n\n")
            print(f"PLAYER [0]'S MAP\n{arr_to_str(map0)}\n")
            print(f"PLAYER [1]'S MAP\n{arr_to_str(map1)}\n")
            exit()

    if game_result != "ended":
        print("GAME OVER! DRAW\n")
        print(f"PLAYER [0]'S MAP\n{arr_to_str(map0)}\n")
        print(f"PLAYER [1]'S MAP\n{arr_to_str(map1)}\n")


if __name__ == "__main__":
    main()
