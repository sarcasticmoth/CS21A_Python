"""
    Vanessa Ulloa
    CS21A
    27 November 2018
    Assignment 9
"""

from hand import Hand
import pickle

# This file tests the Hand class by testing the constructor
# hitMe(), bjValue() and str() methods
# Multiple hand objects are created.

# Test Class
if __name__ == "__main__":
    print("___Testing Hand Class___")
    h1 = Hand(3)
    print(h1)
    print(h1.bjValue())
    h1.hitMe()
    print(h1)
    print(h1.bjValue())

    print()
    h2 = Hand(2)
    print(h2)
    print(h1)   # verifies that the creation of h2 did not effect h1

    print("___Addition Test Cases___")
    # Test a hand with no cards
    # and increase the number of cards and verify the bjValue() return value
    h3 = Hand(0)
    print(h3)
    print(h3.bjValue())

    h3.hitMe()
    print(h3)
    print(h3.bjValue())
    h3.hitMe()
    print(h3)
    print(h3.bjValue())
    h3.hitMe()
    print(h3)
    print(h3.bjValue())

    print("___EXTRA CREDIT___")
    # take a Hand object and store in a pickle file.
    # the contents of this pickle file are retrived and stored
    # into a new hand object.
    # the original hand object and the new object are compared to verify
    # the objects are identical by comparing the bjValue() of each hand
    extraCreditFile = open('hand.pkl', 'wb')
    pickle.dump(h1, extraCreditFile)
    extraCreditFile.close()

    extraCreditFile = open('hand.pkl', 'rb')
    h4 = pickle.load(extraCreditFile)

    print("\n**Pickle Test**")
    print(h1)
    print(h4)

    if h1.bjValue() == h4.bjValue():
        print("Contents of h1 and h4 match!")


# Output
'''
___Testing Hand Class___
8 of Diamonds
9 of Spades
Ace of Spades

18
8 of Diamonds
9 of Spades
Ace of Spades
6 of Spades

24

4 of Diamonds
7 of Clubs

8 of Diamonds
9 of Spades
Ace of Spades
6 of Spades

___Addition Test Cases___
no cards
0
Jack of Hearts

10
Jack of Hearts
2 of Hearts

12
Jack of Hearts
2 of Hearts
8 of Hearts

20
___EXTRA CREDIT___

**Pickle Test**
8 of Diamonds
9 of Spades
Ace of Spades
6 of Spades

8 of Diamonds
9 of Spades
Ace of Spades
6 of Spades

Contents of h1 and h4 match!
'''