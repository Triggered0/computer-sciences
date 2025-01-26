def get_input():
    numbers = input('Enter a list of numbers seperated by ":"\n')
    try:
        numbers = numbers.split(":")
        numbers = [int(i) for i in numbers]
        return numbers
    except:
        print("Invalid input")
        return get_input()


def main():
    data = get_input()
    first = [i for i in data if i != max(data) and i != min(data)] or ["None"]
    second = [i for i in data if i % 2 == 0] or ["None"]
    third = [i for i in data if i > 9 and i < 100] or ["None"]

    print(
        f"""
I. {":".join(str(i) for i in first)}
II. {":".join(str(i) for i in second)}
III. {":".join(str(i) for i in third)}
"""
    )


if __name__ == "__main__":
    main()
