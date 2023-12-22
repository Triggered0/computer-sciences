# Load a list of quotes. Each quote is represented by a dictionary with fields 'author' and 'text'. 'text' is the quote text represented on a single line (as a string)
def loadQuotes(fname):

    f = open(fname)

    lQuotes = []
    
    author = f.readline()
    while author != '':
        quote = ''
        line = f.readline().strip() # After a quote we can either have a line with just '\n' or an empty string '' (end of file). With strip() we unify the two cases, and we can use a single control in the while below
        while line != '':
            quote = quote + line + ' '
            line = f.readline().strip()
        lQuotes.append({
            'author': author.strip(),
            'text': quote.strip()
        })
        author = f.readline()
        
    f.close()
    
    return lQuotes

# Load the topics as a set of strings
def loadTopics(fname):

    f = open(fname)
    sTopics = set()
    for line in f:
        sTopics.add(line.strip().lower())
    f.close()
    return sTopics

# Given a quote :quote:, extract the cleaned list of words from the quote text
def extractWordsFromQuote(quote):
    text = quote['text']
    wordList = text.split()
    cleanedWordList = []
    for word in wordList:
        cleanedWordList.append(word.strip(",.;:'()\"").lower())
    return cleanedWordList

# Print a quote according to the specified format
def printQuote(quote):

    author = quote['author']
    text = quote['text']
    if len(text) > 50:
        text = text[0:50] + '...'
    print (author, "-", text)

# Filter quotes and print those contain any word in the set of topics
def selectAndPrintQuotes(lQuotes, sTopics):
    for quote in lQuotes:
        quoteWordList = extractWordsFromQuote(quote)
        toPrint = False
        for topic in sTopics:
            if topic in quoteWordList:
                toPrint = True
                break
        if toPrint:
            printQuote(quote)

# Filter quotes and print those contain any word in the set of topics - alternative solution
def selectAndPrintQuotes_v2(lQuotes, sTopics):
    for quote in lQuotes:
        quoteWordSet = set(extractWordsFromQuote(quote))
        if len(quoteWordSet.intersection(sTopics)) > 0:
            printQuote(quote)
            
def main():

    lQuotes = loadQuotes('quotes.txt')
    sTopics = loadTopics('topics.txt')
    selectAndPrintQuotes(lQuotes, sTopics)
    #selectAndPrintQuotes_v2(lQuotes, sTopics)

main()
    
