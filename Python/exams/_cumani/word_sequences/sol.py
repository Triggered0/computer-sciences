# Normalize a word: strip punctuation marks and convert to uppercase
def normalizeWord(word):
    return word.strip(",.!?:;").upper()

# Check if all words in a sequence have the same length as the first
def checkSequence(t):
    for w in t[1:]:
        if len(w) != len(t[0]):
            return False
    return True

# Print a sequence in the desired format
def printSequence(seq):
    print ("(", end = "")
    print ("'%s'" % seq[0], end = '')
    for w in seq[1:]:
        print(", '%s'" % w, end = '')
    print (")")

# Find all squences of length n with words of the same length
def processWords(filename, n):

    f = open(filename)
    
    lastSequence = [] # We use a list to store the last n read words. At the beginning of the program the list is empty. We will keep filling it until it has n elements, and then, for each new word, we will remove the oldest (position 0) and append the new word
    for line in f:
        for word in line.split():
            normWord = normalizeWord(word)
            if len(lastSequence) == n: # If the list has at least n elements, then we need to remove the element in position 0 (oldest word) and add at the end the word we just read.
                lastSequence.pop(0)
            lastSequence.append(normWord)
            if len(lastSequence) == n and checkSequence(lastSequence): # We need to check the size of the list because we may nothave read n words yet
                printSequence(lastSequence) # alternatively: print(tuple(lastSequence))
    f.close()

N = 3
def main():
    
    processWords("text.txt", N)
                
main()
