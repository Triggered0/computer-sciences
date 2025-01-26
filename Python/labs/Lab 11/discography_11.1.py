def read_file(file):
    """Reads the file and returns the content of the file"""
    
    with open(file, encoding="utf-8") as f:
        return f.read()


def get_info(files):
    """Gets the info from the database and returns it as an array"""
    
    info = dict()
    for file in files:
        id, name = file.split(";")
        song_data = read_file(name).splitlines()
        for content in song_data:
            year, title = content.split(";")
            info[year] = info.get(year, [])
            info[year].append((title, id))
    info = sorted(info.items(), key=lambda x: x[0])
    return info


def main():
    """Prints the data in desired format"""
    
    files = read_file("artists.txt").splitlines()
    info = get_info(files)
    for i in info:
        year, data = i
        print(f"{year}:")
        for name, id in data:
            print(f"{name:<30} {id}")


if __name__ == "__main__":
    main()
