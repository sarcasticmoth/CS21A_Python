
from card import Card
import random

# One object of this class represents one hand
# which consists of multiple Card objects
class Hand:

    # collection of cards
    hand = []

    # default constructor that accepts an int value
    # for the num of cards in hand or num of
    # Card objects
    def __init__(self, numCardsInHand):
        if type(numCardsInHand) != int:
            raise TypeError()

        self.numCards = numCardsInHand
        self.hand = []

        if self.numCards != 0:
            for card in range(self.numCards):
                self.hitMe()

    # method to get all the blackjack values for each card
    # in the hand. uses the bjValue method from the Card class
    def bjValue(self):
        bjTotal = 0
        for card in self.hand:
            bjTotal += card.bjValue()
        return bjTotal

    # display all string values of each card in the hand
    def __str__(self):
        theHand = ""
        if len(self.hand) == 0:
            theHand += "no cards"
        else:
            for card in self.hand:
                theHand += str(card) + "\n"
        return theHand

    # add another card in the hand
    def hitMe(self):
        newCard = Card(random.randint(1, 13), random.choice("dchs"))
        self.hand.append(newCard)

