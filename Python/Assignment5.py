"""
    Vanessa Ulloa
    CS21A
    29 October 2018
    Assignment 5
"""
from enum import Enum

# Develop an object-orientated program
# Define a card class

# enums for suit
class Suit(Enum):
    diamonds = 'd'
    clubs = 'c'
    spades = 's'
    hearts = 'h'

# Enum for the card rank
class Rank(Enum):
    Ace = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13

# Defines a class Card
class Card:

    # default constructor for the Card class
    # that accepts values for rank and suit
    # used to create an object of Card
    def __init__(self, rank, suit):
        # sets the rank and suit based on passed parameters
        self.rank = rank
        self.suit = suit

    # returns the rank of the card
    def getRank(self):
        return self.rank.value

    # returns the suit of the card
    def getSuit(self):
        return self.suit.value

    # returns the blackjack value of the card
    def bjValue(self):
        if self.rank.value < 10:
            return self.rank.value
        else:
            return 10

    # returns a string of the name of the card
    def __str__(self):
        return "%s of %s" % (self.rank.name, self.suit.name)

# Test Program: #
# Create two Card objects

# testing default constructor
defaultCard = Card(Rank.Ace, Suit.spades)
print(defaultCard)
print(defaultCard.getRank())
print(defaultCard.getSuit())
print(defaultCard.bjValue())
print()

# testing two additional objects
card1 = Card(Rank.Queen, Suit.hearts)
print(card1)
print(card1.getRank())
print(card1.getSuit())
print(card1.bjValue())
print()

card2 = Card(Rank.Six, Suit.clubs)
print(card2)
print(card2.getRank())
print(card2.getSuit())
print(card2.bjValue())

