err_count = 0
values = []

while True:
    if err_count < 2:
        x = input("Enter a float: ")

        if x == "":
            print(f"Values: {values}\nSum: {sum(values)}")
            exit()

        try:
            to_float = float(x)
            values.append(to_float)
        except ValueError as e:
            err_count += 1
            print(f"wrong input count: {err_count}")

    else:
        exit()
