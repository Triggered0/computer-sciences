def createRecord(line):

    fields = line.strip().split(':')
    record = {
        'name': fields[0],
        'id': fields[1],
        'rooms': int(fields[2]),
        'price': float(fields[3]),
        'freeRooms': int(fields[2]),
    }
    return record

def readHotels(filename):

    f = open(filename)
    hHotels = {}
    
    for line in f:
        hotel = createRecord(line)
        hHotels[hotel['id']] = hotel

    f.close()

    return hHotels

def processSingleBooking(hHotels, hotelId, nRooms):

    if hotelId not in hHotels:
        return False
    if hHotels[hotelId]['freeRooms'] < nRooms:
        return False
    hHotels[hotelId]['freeRooms'] = hHotels[hotelId]['freeRooms'] - nRooms
    return True

def processAllBookings(filename, hHotels):

    f = open(filename)

    nConfirmed = 0
    nUnconfirmed = 0
    
    for line in f:
        fields = line.split()
        hotelId = fields[1]
        nRooms = int(fields[2])
        if processSingleBooking(hHotels, hotelId, nRooms):
            nConfirmed = nConfirmed + 1
        else:
            nUnconfirmed = nUnconfirmed + 1
            print ("Unconfirmed booking:", fields[0])
    print ("Confirmed bookings: %d - Unconfirmed bookings: %d" % (nConfirmed, nUnconfirmed))
    
    f.close()
    
    return

def findEmptiestHotel(hHotels):

    maxHotelId = None
    for hotelId in hHotels:
        if maxHotelId == None or hHotels[hotelId]['freeRooms'] > hHotels[maxHotelId]['freeRooms']:
            maxHotelId = hotelId
    return maxHotelId

def printHotels(hHotels):

    print("Hotels status:")
    for hotelId in hHotels:
        hotel = hHotels[hotelId]
        print("    %s: %d rooms (%d free)" % (hotel['name'], hotel['rooms'], hotel['freeRooms']))

def main():

    hHotels = readHotels("hotels.txt")
    processAllBookings("bookings.txt", hHotels)
    print()
    printHotels(hHotels)
    print()
    print("Hotel with more free rooms:", hHotels[findEmptiestHotel(hHotels)]['name'])

main()
    
