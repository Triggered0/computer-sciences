FILE = "herald_of_darkness.txt"


def get_song(file):
    try:
        with open(file) as f:
            data = f.read().split("\n")
            song = dict()
            for line in data:
                character, quote = line.split(": ")
                character = character.casefold()
                song[character] = song.get(character, [])
                song[character].append(quote)
            return song
    except OSError:
        exit("File not found")


def get_character(song):
    character = input("Enter a character: ").casefold()
    while character not in song:
        print("Character not found")
        character = input("Enter a character: ").casefold()
    return character


def main():
    data = get_song(FILE)
    character = get_character(data)
    quotes = "\n".join(data[character])
    print(f"{character.title()} says:\n{quotes}")


if __name__ == "__main__":
    main()
