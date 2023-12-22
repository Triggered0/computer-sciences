# This solution requires knowing N in advance (can be modified to work without knowing N, but then it would need to read the file twice)

# Create an empty table of records of size n x n
def emptyTable(n):

    table = []
    for i in range(n):
        table.append([0] * n)
    return table

# Given a line of the file, extract the corresponding record
def createRecord(line):
    fields = line.split()
    record = {
        'time': fields[0],
        'x': int(fields[1]),
        'y': int(fields[2]),
        'temp': float(fields[3])
    }
    return record

def loadAndProcess(filename, n):

    f = open(filename)

    tempTable = emptyTable(n)
    countTable = emptyTable(n)

    maxRecord = None
    
    for line in f:
        record = createRecord(line)
        x = record['x']
        y = record['y']
        
        tempTable[x][y] = tempTable[x][y] + record['temp']
        countTable[x][y] = countTable[x][y] + 1

        if maxRecord == None or record['temp'] > maxRecord['temp']:
            maxRecord = record

    f.close()
    
    print ("Temperature averages:")
    for x in range(n):
        for y in range(n):
            if (countTable[x][y] > 0):
                print ("(%d, %d) %.1f" % (x, y, tempTable[x][y] / countTable[x][y]))

    print()
    print ("Maximum value was measured by sensor (%d, %d) at %s" % (maxRecord['x'], maxRecord['y'], maxRecord['time']))
    
def main():

    N = 2
    loadAndProcess('sensors.txt', N)

main()
