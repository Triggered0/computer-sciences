# Events are stored in a dictionary. The key is the day, while values are lists of tuples (time, event) of the events of each day.

# The function checks whether the slot (day, time) is free, returning True if it is and False otherwise
def checkFreeSlot(hEvents, day, time):

    if day not in hEvents:
        return True # Day not present, sol the slot is free
    
    for eventTuple in hEvents[day]:
        if eventTuple[0] == time:
            return False # An event is already present at the given time
        
    return True # No event was found in theprevious loop, so there are no events in the requested slot

# Insert a new event, checking if the slot is free. The function returns a boolena value. True means the event was allocated, False means it was not possible to allocate the event.
def insertEvent(hEvents, day, time, event):
    
    if checkFreeSlot(hEvents, day, time):
        if day not in hEvents:
            hEvents[day] = []
        hEvents[day].append( (time, event) )
        return True
    else:
        return False

# Load events fromt a file, building the events dictionary.
def loadEvents(filename):

    f = open(filename)
    hEvents = {}
    for line in f:
        fields = line.strip().split(';')
        
        day = int(fields[0])
        time = int(fields[1])
        event = fields[2]
        insertEvent(hEvents, day, time, event)

    f.close()
        
    return hEvents

# Print the events of a day, or notify that there are on events on a given day
def visualizeEvents(hEvents, day):

    if day not in hEvents:
        print("No events on day", day)
        return

    print("Events of day %d:" % day)
    for eventTuple in sorted(hEvents[day]):
        time = eventTuple[0]
        event = eventTuple[1]
        print("  %02d: %s" % (time, event))
        
    return

# Extract the event name removing the first 3 fields of the command. <s> is the line that contains the insertion command
def extractEventName(s):
    s = s.strip() # remove blanks before the command (i) and after the event (end of the line)
    fields = s.split()
    s = s[len(fields[0]):].strip() # remove the "i" part of the command, and remove all following blanks
    s = s[len(fields[1]):].strip() # remove the day field, and strip all following blanks
    s = s[len(fields[2]):].strip() # remove the time field, and strip all followinf blanks
    return s # what remains is the string corresponding to the event

# Parse the commands file, executing the commands using the dictionary hEvents
def parseCommands(hEvents, filename):

    f = open(filename)
    for line in f:
        fields = line.strip().split(maxsplit=3) # Should we not remember how maxsplit works, we can simply use split() here and use the commented code below to extract the event
        command = fields[0]
        if command == 'v':
            day = int(fields[1])
            visualizeEvents(hEvents, day)
        elif command == 'i':
            day = int(fields[1])
            time = int(fields[2])
            event = fields[3]
            # Should we not rememeber how maxsplit works, we can replace
            # event = fields[3]
            # with
            # event = extractEventName(line)
            if insertEvent(hEvents, day, time, event):
                print("Event inserted")
                visualizeEvents(hEvents, day)
            else:
                print("Cannot insert event")
    f.close()
    return

def main():

    hEvents = loadEvents("events.txt")
    parseCommands(hEvents, "commands.txt")

main()
