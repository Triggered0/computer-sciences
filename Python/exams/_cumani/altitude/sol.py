def loadMap(filename):

    t = []
    f = open(filename)
    for line in f:
        row = []
        for val in line.split():
            row.append(int(val))
        t.append(row)

    return t

def isValid(t, row, col):
    nRow = len(t)
    nCol = len(t[0])
    if row < 0 or col < 0 or row >= nRow or col >= nCol:
        return False
    return True

def isMaximum(t, row, col):
    nRow = len(t)
    nCol = len(t[0])

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if (i != 0 or j != 0) and isValid(t, row + i, col + j) and t[row + i][col + j] >= t[row][col]: # (i != 0 or j != 0) is required to avoid checking the cell in position (row, col) - the condition corresponds to not (i==0 and j==0)
                return False
    return True


def main():
    
    m = loadMap("map.txt")
    nMax = 0
    totMax = 0
    for row in range(len(m)):
        for col in range(len(m[row])):
            if isMaximum(m, row, col) and m[row][col] > 0:
                print (m[row][col], row, col)
                nMax = nMax + 1
                totMax = totMax + m[row][col]
    if nMax == 0:
        print("No maxima")
    print()
    if nMax > 0:
        print("Average height:", totMax / nMax, 'm')
        
        
main()
