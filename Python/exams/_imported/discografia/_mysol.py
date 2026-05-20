def read_file(file_name):
    try:
        with open(file_name) as f:
            file_data = []
            data = f.read()
            lines = data.splitlines()

            for line in lines:
                file_data.append(line.split(";"))

            return file_data

    except OSError as error:
        print(f"we have an error: {error}")


def main():
    song_data = dict()
    artists = read_file("artists.txt")

    for files in artists:
        data = read_file(files[1])

        for line in data:
            line.append(files[0])
            year, title, code = line
            song_data[year] = song_data.get(year, [])
            song_data[year].append(f"{title} / {code}")

    print(song_data)
    print(song_data.items())

    for year, songs in sorted(song_data.items()):
        print(f"{year}:")
        for song in songs:
            title, code = song.split(" / ")
            print(f"{title:<40} {code}")


if __name__ == "__main__":
    main()
