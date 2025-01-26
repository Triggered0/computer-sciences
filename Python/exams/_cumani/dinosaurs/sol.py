# Read the deck, distributing cards to each player. The players deck are represented by lists, with cards having the same order as in the file.
# Since the text specifies that the player cards are to be played in the same order as they appear in the file, the first element of each list will be the first card to play.
def readDeck(fIn):

    cardsPlayer1 = []
    cardsPlayer2 = []
    player = 1
    for line in fIn:
        card = line.strip()
        if player == 1:
            #cardsPlayer1.insert(0, card)
            cardsPlayer1.append(card)
            player = 2
        else:
            #cardsPlayer2.insert(0, card)
            cardsPlayer2.append(card)
            player = 1
    return cardsPlayer1, cardsPlayer2

# Convert a card to the corresponding score. The score will be also used to sort the card by strength (red > yellow > green). This allows deciding which card wins by a simple comparison of integers
def card2score(c):

    hScore = {
        'Red': 5,
        'Green': 3,
        'Yellow': 1,
        }
    if c in hScore:
        return hScore[c]
    return None


def main():

    #f = open("deck.txt")
    f = open("deckSmall.txt") # Uncomment this to load the small deck
    cardsPlayer1, cardsPlayer2 = readDeck(f)
    f.close()

    # Table is a list containing the cards on the table, including the last two played (at the beginning it's empty since we didn't play any card)
    table = []
    score1 = 0
    score2 = 0

    idx = 1 # Used for printing the number of each hand

    print ("Player 1 score: 0")
    print ("Player 2 score: 0")
    print()
    
    while len(cardsPlayer1) > 0:
        # Play the cards on top of the deck, corresponding to the first element of the list
        card1 = cardsPlayer1.pop(0)
        card2 = cardsPlayer2.pop(0)
        # The played cards are on the table, we add them to the table list
        table.append(card1)
        table.append(card2)

        # Compare the cards according to their strength - convert each card to the corresponding strength for the comparison
        if card2score(card1) > card2score(card2):
            winner = 'Player 1'
            # Assign all cards on the table to player 1, updating the correspoding score
            for c in table:
                score1 = score1 + card2score(c)
            table = []
        elif card2score(card2) > card2score(card1):
            winner = 'Player 2'
            # Assign all cards on the table to player 2, updating the correspoding score
            for c in table:
                score2 = score2 + card2score(c)
            table = []
        else:
            winner = None

        print ("Hand", idx)
        print ("Player 1's card:", card1)
        print ("Player 2's card:", card2)

        if winner  == None:
            print ("Result: draw")
        else:
            print ("Result:", winner, "wins the hand")
        
        print ("Player 1's score:", score1)
        print ("Player 2's score:", score2)
        print ()

        idx = idx + 1

    if score1 > score2:
        print ("Player 1 wins with %d points" % score1)
    elif score1 < score2:
        print ("Player 2 wins with %d points" % score2)
    else:
        print ("The match is a draw")
            
            
main()
