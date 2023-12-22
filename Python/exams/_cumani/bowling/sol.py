# Read the score files in a list of dictionaries
def readBowlingScores(fname):

    f = open(fname)

    lPlayers = []
    for line in f:
        fields = line.strip().split(';')
        surname = fields[0]
        name = fields[1]
        scores = []
        for i in fields[2:]:
            scores.append(int(i))
        lPlayers.append({'surname': surname, 'name': name, 'scores': scores})

    f.close()
    
    return lPlayers

# Version 1

# To sort, we use as key the total scores of a player. The sortKey function computes, given a player, the total score
def sortKey_v1(player):
    return sum(player['scores'])

# Print the sorted leaderboard
def printLeaderboard_v1(lPlayers):

    lPlayersSorted = sorted(lPlayers, key = sortKey_v1)[::-1]
    for player in lPlayersSorted:
        print (player['surname'], player['name'], sortKey_v1(player))

# Count how many times a player :player: scored a score :val: 
def countScores(player, val):
    n = 0
    for i in player['scores']:
        if i == val:
            n = n + 1
    return n

# print the player who scored a given score most times
def printMostScores(lPlayers, score):

    # We initalize the maximum searcgh with the information of the first player.  We track the number of scores equal to :score: as to avoid calling the function countScores an unnecessary number of times inside the loop
    idxMax = 0
    n = countScores(lPlayers[0], score)
    
    for playerIdx in range(1, len(lPlayers)):
        player = lPlayers[playerIdx]
        np = countScores(player, score)
        if np > n:
            idxMax = playerIdx
            n = np
    if n > 1:
        print ('Most %d:' % score, lPlayers[idxMax]['surname'], lPlayers[idxMax]['name'], '(%d times)' % n)
    elif n > 0:
        print ('Most %d:' % score, lPlayers[idxMax]['surname'], lPlayers[idxMax]['name'], '(%d time)' % n)
    else:
        print ('No player scored %d' % score)

def main():

    lPlayers = readBowlingScores('bowling.txt')
    printLeaderboard_v1(lPlayers)
    printMostScores(lPlayers, 10)
    printMostScores(lPlayers, 0)
     
# Version 2 - we fill the players info with the total and use the additioanl field to sort the list

# Add the total score to each dictionary in the list :lPLayers:
def fillTotalScore(lPlayers):
    for player in lPlayers:
        player['total'] = sum(player['scores'])

def sortKey_v2(player):
    return player['total']

def printLeaderboard_v2(lPlayers):
    lPlayersSorted = sorted(lPlayers, key = sortKey_v2)[::-1]
    for player in lPlayersSorted:
        print (player['surname'], player['name'], player['total'])

def main_v2():

    lPlayers = readBowlingScores('bowling.txt')
    fillTotalScore(lPlayers)
    printLeaderboard_v2(lPlayers)
    printMostScores(lPlayers, 10) # This is the same as in the first version
    printMostScores(lPlayers, 0) # This is the same as in the first version

# Uncomment only one version
main()
#main_v2()
    
    

    
