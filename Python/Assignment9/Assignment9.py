"""
    Vanessa Ulloa
    CS21A
    27 November 2018
    Assignment 9
"""

from card import Card

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

# OUTPUT
