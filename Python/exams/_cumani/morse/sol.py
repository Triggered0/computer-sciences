def readCodeFile(fname):

    f = open(fname)
    hChar2Code = {}
    for line in f:
        fields = line.strip().split()
        if len(fields) == 2:
            char = fields[0]
            code = fields[1]
            hChar2Code[char] = code
    f.close()
            
    return hChar2Code

def buildReverseCode(hChar2Code):
    
    hCode2Char = {}
    for char in hChar2Code:
        code = hChar2Code[char]
        hCode2Char[code] = char
    return hCode2Char

def encodeFile(filename, hChars2Codes):
    f = open(filename)
    line = f.readline().upper()
    if len(line) > 0:
        if line[0] in hChars2Codes:
            print(hChars2Codes[line[0]], end = "")
        for char in line[1:]:
            if char in hChars2Codes:
                print (" " + hChars2Codes[char], end = "")
    print()
    f.close()

def decodeFile(filename, hCodes2Chars):
    f = open(filename)
    line = f.readline()
    fields = line.split()
    if len(fields) > 0:
        if fields[0] in hCodes2Chars:
            print(hCodes2Chars[fields[0]], end="")
        for code in fields[1:]:
            if code in hCodes2Chars:
                print(hCodes2Chars[code], end="")
    print()
    f.close()

def main():

    hChar2Code = readCodeFile('morse.txt')
    hCode2Char = buildReverseCode(hChar2Code)

    f = open("commands.txt")

    for line in f:
        fields = line.split()
        if len(fields) == 2:
            command = fields[0]
            filename = fields[1]
            if command == 'd':
                print ("Decoding file %s:" % filename)
                decodeFile(filename, hCode2Char)
            elif command == 'e':
                print ("Encoding file %s:" % filename)
                encodeFile(filename, hChar2Code)

    f.close()
        
main()
