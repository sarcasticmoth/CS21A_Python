"""
    Vanessa Ulloa
    CS21A
    29 October 2018
    Assignment 5
"""
# Develop an object-orientated program
# Define a card class

# Defines a class Card
class Card:
    # default constructor for the Card class
    # that accepts values for rank and suit
    # used to create an object of Card
    def __init__(self, rank, suit):
        # sets the rank and suit based on passed parameters
        self.rank = rank
        self.suit = suit
        Card.ranks = [None, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        Card.suits = {
            "s" : "Spades",
            "d" : "Diamonds",
            "c" : "Clubs",
            "h" : "Hearts"
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

# Test Program: #
# Create two Card objects

# testing default constructor
defaultCard = Card(1, "s")
print(defaultCard)
print(defaultCard.getRank())
print(defaultCard.getSuit())
print(defaultCard.bjValue())
print()

# testing two additional objects
card1 = Card(12, "h")
print(card1)
print(card1.getRank())
print(card1.getSuit())
print(card1.bjValue())
print()

card2 = Card(6, "c")
print(card2)
print(card2.getRank())
print(card2.getSuit())
print(card2.bjValue())

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

Process finished with exit code 0

"""
