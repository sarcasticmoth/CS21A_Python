"""
    Vanessa Ulloa
    CS21A
    07 November 2018
    Assignment 6
"""

# use the Card class from assignment 5
# add exception handlers

class Card:
    # default constructor for the Card class
    # that accepts values for rank and suit
    # used to create an object of Card
    def __init__(self, rank, suit):
        # sets the rank and suit based on passed parameters
        # check to make sure rank is of type int or
        if type(rank) != int:
            raise TypeError()

        if type(suit) != str:
            raise TypeError()

        # check if values are part of the list and dictionary
        if rank < 1 or rank > 13:
            raise ValueError()

        if suit not in ['s', 'd', 'c', 'h']:
            raise ValueError()

        self.rank = rank
        self.suit = suit
        Card.ranks = [None, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        Card.suits = {
            's': "Spades",
            'd': "Diamonds",
            'c': "Clubs",
            'h': "Hearts"
        }

    # returns the rank of the card
    def getRank(self):
        return self.rank

    # returns the suit of the card
    def getSuit(self):
        return self.suit

    # returns the blackjack value of the card
    def bjValue(self):
        if self.rank < 10:
            return self.rank
        else:
            return 10

    # gets the card value

    # returns a string of the name of the card
    def __str__(self):
        return "%s of %s" % (Card.ranks[self.rank], Card.suits.get(self.suit))


# testing default constructor
try:
    defaultCard = Card(1, "s")
except:
    print("error creating card")
else:
    print(defaultCard)
    print(defaultCard.getRank())
    print(defaultCard.getSuit())
    print(defaultCard.bjValue())
    print()

# testing two additional objects
try:
    card1 = Card(12, "h")
except:
    print("error creating card")
else:
    print(card1)
    print(card1.getRank())
    print(card1.getSuit())
    print(card1.bjValue())
    print()

try:
    card2 = Card(6, "c")
except:
    print("error creating card")
else:
    print(card2)
    print(card2.getRank())
    print(card2.getSuit())
    print(card2.bjValue())
    print()

# test passing two string values
try:
    card3 = Card("d", "d")
except:
    print("error creating card")
else:
    print(card3)
    print(card3.getRank())
    print(card3.getSuit())
    print(card3.bjValue())
    print()

# test passing two int values
try:
    card6 = Card(4, 4)
except:
    print("error creating card")
else:
    print(card6.getRank())
    print(card6.getSuit())
    print(card6.bjValue())
    print()

# test a rank that outside of the allowed values
try:
    card4 = Card(16, "h")
except:
    print("error creating card")
else:
    print(card4)
    print(card4.getRank())
    print(card4.getSuit())
    print(card4.bjValue())
    print()

# test a suit that is outside of the allowed values
try:
    card5 = Card(4, "x")
except:
    print("error creating card")
else:
    print(card5.getRank())
    print(card5.getSuit())
    print(card5.bjValue())
    print()

# Output
"""
Ace of Spades
1
s
1

Queen of Hearts
12
h
10

6 of Clubs
6
c
6

error creating card
error creating card
error creating card
error creating card

Process finished with exit code 0
"""