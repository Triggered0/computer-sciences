""" import re

index = []
even = []

x = input("String: ")
arr = list(x)

for i in range(len(arr)):
    if i % 2 == 1:
        even.append(arr[i])

    if re.search("[aeiouAEIOU]", arr[i]):
        index.append(str(i))

match = re.findall("[A-Z]", x)
match = "".join(match)
even = "".join(even)
vowels = re.sub("[aeiouAEIOU]", "_", x)
length = len(x)
index = " ".join(index)

print(
    f"Only Capitals: {match}\nEven Positions: {even}\nReplace Vowels: {vowels}\nLength: {length}\nVowels Indexes: {index}"
) """

##################################################################################################################################

index = []
even = []
upper = []
vowels = []
vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]


x = input("String: ")
arr = list(x)
replace = list(x)

for i in range(len(arr)):
    if i % 2 == 1:
        even.append(arr[i])

    if arr[i] in vowel:
        vowels.append(arr[i])
        index.append(str(i))
        replace[i] = "_"
    if arr[i].isupper():
        upper.append(arr[i])

upper = "".join(upper)
even = "".join(even)
vowels = "".join(replace)
length = len(x)
index = " ".join(index)

print(
    f"Only Capitals: {upper}\nEven Positions: {even}\nReplace Vowels: {vowels}\nLength: {length}\nVowels Indexes: {index}"
)
