FILE = "lonely_boy.txt"

str_to_token = dict()
token_to_str = dict()


def read_file(file):
    """Reads a file and returns the contents as a string."""

    try:
        with open(file) as f:
            return f.read()
    except OSError as error:
        exit(f"We have a problem:\n{error}")


def intern_string(text):
    """Returns an integer token for the string."""

    str_to_token[text] = str_to_token.get(text, len(str_to_token))
    token_to_str[str_to_token[text]] = text
    return str_to_token[text]


def get_string(token):
    """Returns the string for the token."""

    return token_to_str[token]


def main():
    """Prints the token and string for each line in the file."""

    data = read_file(FILE).splitlines()

    for line in data:
        print(f"Token: {intern_string(line)} - {get_string(intern_string(line))}")


if __name__ == "__main__":
    main()
