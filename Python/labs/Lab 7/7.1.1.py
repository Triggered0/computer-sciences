def count_words(s):
    data = s.split(" ")
    words = dict()
    for i in data:
        if i in words:
            words[i] += 1
        else:
            words[i] = 1
    print(words)
