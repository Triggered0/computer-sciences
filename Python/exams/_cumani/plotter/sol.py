# Plot a table t
def plotTable(t):
    for row in t:
        for col in row:
            print(col, end = "")
        print()

# Check if a coordinate is valid
def checkCoord(t, row, col):
    if row < 0 or col < 0 or row >= len(t) or col >= len(t[row]):
        return False
    return True

# Draw a single point
def drawPoint(t, row, col):

    if not checkCoord(t, row, col):
        return
    t[row][col] = '*'

# Draw a horizontal line
def drawHLine(t, row, col, l):

    for i in range(l):
        if not checkCoord(t, row, col + i):
            return
        if t[row][col + i] == '|':
            t[row][col + i] = '+'
        else:
            t[row][col + i] = '-'

# Draw a vertical line            
def drawVLine(t, row, col, l):

    for i in range(l):
        if not checkCoord(t, row - i, col):
            return
        if t[row - i][col] == '-':
            t[row - i][col] = '+'
        else:
            t[row - i][col] = '|'

# Create the inital table
def createTable(nRows, nCols):

    t = []
    for i in range(nRows):
        t.append(["."] * nCols)
    return t

NROWS = 20 # Set to 5 to get the example plot
NCOLS = 20 # Set to 5 to get the example plot

def main():

    t = createTable(NROWS, NCOLS)
    f = open("plotter.txt")
    for line in f:
        fields = line.strip().split()
        col = int(fields[1])
        row = NROWS - int(fields[2]) - 1 # Since the y-coordinates of the square are reversed with respect tot the row indeces of the square, we convert the y-coordinates to the corresponding row index.
        if fields[0] == 'P':
            drawPoint(t, row, col)
        elif fields[0] == 'H':
            drawHLine(t, row, col, int(fields[3]))
        elif fields[0] == 'V':
            drawVLine(t, row, col, int(fields[3]))

    f.close()
    plotTable(t)

main()
