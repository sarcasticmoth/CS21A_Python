# One object of this class represents one playing card
# with a suit and rank
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

