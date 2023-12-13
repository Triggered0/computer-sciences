def main():
    turn = True
    table = create_table()
    show_table(table)

    while " " in table[0] or " " in table[1] or " " in table[2]:
        player = "X" if turn else "O"
        row, column = get_move(player)

        if table[row - 1][column - 1] == " ":
            table[row - 1][column - 1] = player
            show_table(table)
            win = check_win(table)
            if win == "Draw":
                exit(f"Game Over! - {win}")
            elif win:
                exit(f"Game Over! - {win} wins")
        else:
            print("Invalid move")
            show_table(table)
            continue
        turn = not turn

    exit("Game Over - Draw")


def get_move(player):
    try:
        row, column = input(f"Enter a move Player [{player}] (Ex: 1,2): \n").split(",")
        row, column = int(row), int(column)
        if not check_input(row, column):
            raise Exception
        return row, column
    except:
        print("Invalid input")
        return get_move(player)


def create_table():
    table = []
    for i in range(3):
        table.append([" "] * 3)
    return table


def check_input(row, column):
    if row < 1 or row > 3 or column < 1 or column > 3:
        return False
    return True


def show_table(table):
    print()
    for row in table:
        print(row)
    print()


def check_win(table):
    if table[0][0] == table[0][1] == table[0][2] != " ":
        return table[0][0]
    elif table[1][0] == table[1][1] == table[1][2] != " ":
        return table[1][0]
    elif table[2][0] == table[2][1] == table[2][2] != " ":
        return table[2][0]
    elif table[0][0] == table[1][0] == table[2][0] != " ":
        return table[0][0]
    elif table[0][1] == table[1][1] == table[2][1] != " ":
        return table[0][1]
    elif table[0][2] == table[1][2] == table[2][2] != " ":
        return table[0][2]
    elif table[0][0] == table[1][1] == table[2][2] != " ":
        return table[0][0]
    elif table[0][2] == table[1][1] == table[2][0] != " ":
        return table[0][2]
    elif " " not in table[0] and " " not in table[1] and " " not in table[2]:
        return "Draw"
    else:
        return False


if __name__ == "__main__":
    main()
