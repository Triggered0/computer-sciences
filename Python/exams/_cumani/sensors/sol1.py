# This solution does not require knowing N in advance.

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

# Load sensors data in a dictionary of records. The tuple (x, y) is the dictionary key. The corresponding value is the list of readings for that sensor
def loadSensors(filename):

    f = open(filename)
    hSensorMatrix = {}

    for line in f:
        record = createRecord(line)
        x = record['x']
        y = record['y']
        if (x, y) not in hSensorMatrix:
            hSensorMatrix[(x, y)] = []
        hSensorMatrix[(x, y)].append(record)

    f.close()
    
    return hSensorMatrix

# Given a list of readings, compute the average temperature
def computeAverage(recordList):
    tot = 0
    for record in recordList:
        tot = tot + record['temp']
    if len(recordList) > 0:
        return tot / len(recordList)
    return None

# Print the average for each sensor. We need to iterate over sensors (the kesy of the dictionary)
def printAverages(hSensorMatrix):

    print ("Temperature averages:")
    for coord in sorted(hSensorMatrix): # sorted ensures we print in the same order as in the example - not required by the text
        recordList = hSensorMatrix[coord]
        averageTemp = computeAverage(recordList)
        if averageTemp != None:
            print ("(%d, %d) %.1f" % (coord[0], coord[1], averageTemp))

# Print the maximum reading. We need to iterate over all readings, that is, over sensors (outer loop) and, given a sensor, over its readings (inner loop) tot rack the record corresponding to the maximum temperature
def printMax(hSensorMatrix):

    recordMax = None
    for coord in sorted(hSensorMatrix):
        for record in hSensorMatrix[coord]: # sorted may be skipped here, but ensures that we find the lowest (in lexicographical order) sensor in case of multiple maxima
            if recordMax == None or record['temp'] > recordMax['temp']:
                recordMax = record

    print ("Maximum value was measured by sensor (%d, %d) at %s" % (recordMax['x'], recordMax['y'], recordMax['time']))

def main():

    hSensorMatrix = loadSensors("sensors.txt")
    printAverages(hSensorMatrix)
    print()
    printMax(hSensorMatrix)
    
main()
