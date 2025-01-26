import re

x = input("Enter String: ")


def vowels(str):
    match = re.findall("[AEIOUaeiou]", str)
    return len(match)


print(f"Size of Vowels: {vowels(x)}")
