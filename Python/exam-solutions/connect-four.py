FILE_NAME = "mosse.txt"
GAME = dict()


def get_gameinfo(file):
    # gets the data from "mosse.txt" and puts into the GAME dict
    try:
        with open(file, encoding="utf-8") as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                _, index = line.split()
                GAME["moves"] = GAME.get("moves", [])
                GAME["moves"].append(int(index))
            GAME["moves_count"] = len(lines)
        return GAME
    except OSError as err:
        exit(f"ERROR! {err}")


def create_table(row, col):
    # creates the game table and puts the table info to GAME dict
    table = []
    for i in range(row):
        table.append(["-"] * col)

    GAME["row_count"] = row
    GAME["col_count"] = col

    return table


def print_table(table):
    # prints the table as a string
    for line in table:
        print("".join(line))


def check_win(table):
    # checks if anybody wins
    win = False
    row = GAME["row_count"]
    col = GAME["col_count"]

    # horizontal win
    for r in range(row):
        for c in range(col - 3):
            if table[r][c] == table[r][c+1] == table[r][c+2] == table[r][c+3] and not "-":
                win = True
                break
                break

    # vertical win
    if not win:
        for r in range(row - 3):
            for c in range(col):
                if table[r][c] == table[r+1][c] == table[r+2][c] == table[r+3][c] != "-":
                    win = True
                    break
                    break

    # diagonal win
    if not win:
        for r in range(row - 3):
            for c in range(col-3):
                if table[r][c] == table[r+1][c+1] == table[r+2][c+2] == table[r+3][c+3] != "-":
                    win = True
                    break
                    break
                elif table[::-1][r][c] == table[::-1][r+1][c+1] == table[::-1][r+2][c+2] == table[::-1][r+3][c+3] != "-":
                    win = True
                    break
                    break
    return win


def main():
    # play the game
    game = get_gameinfo(FILE_NAME)
    table = create_table(6, 7)

    print("Empty Grid")
    print_table(table)
    print()

    for i in range(game["moves_count"]):
        
        # choose player
        if i % 2 == 0:
            player = "G1"
            sign = "O"
        else:
            player = "G2"
            sign = "X"

        print(f"Player {player} Plays:")

        for j in range(game["row_count"]):
            row = game["row_count"] - 1
            
            #put the sign of the player and check the gravity
            if table[row-j][game["moves"][i]] == "-":
                table[row-j][game["moves"][i]] = sign
                break

        print_table(table)
        print()

        win = check_win(table)

        if win:
            print(f"{player} wins in {i + 1} moves")
            break


if __name__ == "__main__":
    main()
