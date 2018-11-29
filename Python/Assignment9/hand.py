
from card import Card
import random

# One object of this class represents one hand
# which consists of multiple Card objects
class Hand:

    # default constructor that accepts an int value
    # for the num of cards in hand or num of
    # Card objects
    def __init__(self, numCardsInHand):
        if type(numCardsInHand) != int:
            raise TypeError()

        # variable used to store a collection
        # of card objects
        self.hand = []

        # for the numCardsInHand specified, call hitMe()
        # this adds a new card object to the hand
        if numCardsInHand != 0:
            for card in range(numCardsInHand):
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

