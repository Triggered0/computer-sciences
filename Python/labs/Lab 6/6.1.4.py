def read_file(file):
    with open(file) as f:
        return f.read()


def write_file(file, data):
    with open(file, "w") as f:
        return f.writelines(data)


def main():
    try:
        data = read_file("clients.txt")
    except OSError as e:
        exit(f"Error: {e}")

    services = dict()

    for client in data.split("\n"):
        client_data = client.split(";")

        try:
            to_float = float(client_data[2])
        except ValueError as f:
            exit("Wrong file format")

        if len(client_data) != 4:
            exit("Wrong file format")
        elif not isinstance(to_float, float):
            exit("Wrong file format")

        if client_data[1] not in services:
            services[client_data[1]] = 1
        else:
            services[client_data[1]] += 1

    for key, value in services.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
