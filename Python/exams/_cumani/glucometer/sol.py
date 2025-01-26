# Load patietns in a dictionary indexed by <ID>
# A patient is represented as a dictionary with fields
#   * id - the patient ID
#   * readings - a list of readings of that patient
# Each reading is also represented as a dict with fields
#   * time - the reading time (as a string)
#   * index - the glucometer index (as int)
#   * temp - the temperature (not required for the program)
#   * bpm - the heart beats per minuted (not required for the program)
def loadReadings(fname):

    hPatients = {}
    f = open(fname)
    for line in f:
        fields = line.strip().split()
        reading = {
            'time': fields[1],
            'index': int(fields[2]),
            'temp': float(fields[3]), # not actually required
            'bpm': int(fields[4]), # not actually required
        }
        patientId = fields[0]
        if patientId not in hPatients:
            hPatients[patientId] = {
                'id': patientId,
                'readings': []
            }
        hPatients[patientId]['readings'].append(reading)
    f.close()
    return hPatients

THRESHOLD = 200

# Version 1

# Compute, for a patient, the number of times a reading exceeds the threshold
def computeNumberOfExceedingReadings(patient):
    n = 0
    for i in patient['readings']:
        if i['index'] > THRESHOLD:
            n = n + 1
    return n

def printExceedingReadings_v1(hPatients):

    for patient in sorted(hPatients.values(), key = computeNumberOfExceedingReadings)[::-1]:
        for reading in patient['readings']:
            if reading['index'] > THRESHOLD:
                print(patient['id'], reading['time'], reading['index'])

def main_v1():
    hPatients = loadReadings('glucometer.txt')
    printExceedingReadings_v1(hPatients)

# Version 1

# Compute, for a patient, the number of times a reading exceeds the threshold. The value is stored in the patiewnt record
def updateNumberOfExceedingReadings(patient):
    n = 0
    for i in patient['readings']:
        if i['index'] > THRESHOLD:
            n = n + 1
    patient['excessReadings'] = n

def keyExcessReadings(patient):
    return patient['excessReadings']
    
def printExceedingReadings_v2(hPatients):

    for patient in sorted(hPatients.values(), key = keyExcessReadings)[::-1]:
        for reading in patient['readings']:
            if reading['index'] > THRESHOLD:
                print(patient['id'], reading['time'], reading['index'])

def main_v2():
    hPatients = loadReadings('glucometer.txt')
    for k in hPatients:
        updateNumberOfExceedingReadings(hPatients[k])
    printExceedingReadings_v2(hPatients)

# Choose one
main_v1()
#main_v2()
        
    
        
