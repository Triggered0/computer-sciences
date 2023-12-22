TARGET_DATE = "2019-12-21"

# Convert a time to seconds from midnight. Used to compare times
def date2seconds(d):
    fields = d.split(':')
    result = int(fields[0]) * 3600 + int(fields[1]) * 60#
    if len(fields) == 3:
        result = result + int (fields[2])
    return result

# Load the list of users
def loadUsers(filename):

    f = open(filename)
    lUsers = []
    
    for line in f:
        fields = line.split()
        record = {
            'id': fields[0],
            'date': fields[1],
            'entry': fields[2],
            'exit': fields[3],
        }
        lUsers.append(record)
        
    f.close()
    
    return lUsers

# Load the price ranges. These are stored in a dictionary whose keys are the price range names
def loadPrices(filename):

    f = open(filename)
    hPrices = {}

    for line in f:
        fields = line.split()
        record = {
            'name': fields[0],
            'start': fields[1].split('-')[0],
            'end': fields[1].split('-')[1],
            'price': float(fields[2]),
        }
        hPrices[record['name']] = record

    f.close()
    
    return hPrices

# Check if a user (entry, exit) times are in the interval defined for the passed price range
def isInPriceTimeInterval(user, price):
    if date2seconds(price['start']) <= date2seconds(user['entry']) and date2seconds(price['end']) >= date2seconds(user['exit']):
        return True
    return False

# Compute the stats of users for the given date
def computePriceStats(hPrices, lUsers):

    # Dictionary that will contain, for each price range, the number of users that have been charged the corresponding price
    hSummary = {}
    for k in hPrices:
        hSummary[k] = 0

    totalIncome = 0
    nUsers = 0 # Track the number of users on the specific date
    
    for user in lUsers:

        if user['date'] == TARGET_DATE:

            # Search for the best price range
            currentBestPriceKey = None
            for priceKey in hPrices:
                price = hPrices[priceKey]
                if isInPriceTimeInterval(user, price) and (currentBestPriceKey == None or price['price'] < hPrices[currentBestPriceKey]['price']):
                    currentBestPriceKey = priceKey

            bestPrice = hPrices[currentBestPriceKey]
            totalIncome = totalIncome + bestPrice['price']
            nUsers = nUsers + 1
            hSummary[currentBestPriceKey] = hSummary[currentBestPriceKey] + 1
            
            print ('Skipass %s: %s - %.2f EURO' % (user['id'], currentBestPriceKey, bestPrice['price']))

    print()
    print('Total income:', totalIncome)
    print()
    print("User stats:")
    if nUsers > 0:
        for k in hSummary:
            print ('%s: %.1f%%' % (k, hSummary[k] / nUsers * 100))

def main():
    
    lUsers = loadUsers('users.txt')
    hPrices = loadPrices('prices.txt')
    computePriceStats(hPrices, lUsers)

main()
