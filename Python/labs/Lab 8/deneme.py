INDICES_INPUT_FILE = "indices.txt"
OUTPUT_FILE = "indices_strips.txt"


def read_file(filename):
    """reading the file and creating a list of list where to put each line"""
    file = []
    try:
        with open(filename, "r", encoding="utf-8") as input_file:
            for lines in input_file.readlines():
                string = lines.split()
                file.append(string)
            return file
    except OSError as problem:
        print(f"problem => {problem}")


def check(string):
    """checking if numbers are the same and eventually same the last one of the list in the new list otherwise printing error"""
    output_string = [
        string[0][0],
        string[0][1],
        string[0][2],
    ]  # creating a new list with where putting the output numbers
    for n in range(len(string) - 1):
        if string[n][1] == string[n + 1][0] and string[n][2] == string[n + 1][1]:
            output_string.append(string[n + 1][2])
        else:
            print("Yeuch!! We have a problem here!")
    return output_string


def write_output_file(filename, numbs):
    """writing the output file with each numbers of the new list"""
    try:
        with open(filename, "w", encoding="utf-8") as output_file:
            for n in numbs:
                output_file.write(f" {n} ")
            return output_file
    except OSError as problem:
        print(f"problem => {problem}")


def main():
    line = read_file(INDICES_INPUT_FILE)
    final_line = check(line)
    write_output_file(OUTPUT_FILE, final_line)


if __name__ == "__main__":
    main()
