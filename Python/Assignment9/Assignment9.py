"""
    Vanessa Ulloa
    CS21A
    27 November 2018
    Assignment 9
"""

from hand import Hand
import pickle

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
    5 of Hearts
    3 of Hearts
    Queen of Hearts
    
    18
    5 of Hearts
    3 of Hearts
    Queen of Hearts
    Queen of Clubs
    
    28
    
    2 of Diamonds
    8 of Clubs
    
    5 of Hearts
    3 of Hearts
    Queen of Hearts
    Queen of Clubs
    
    ___Addition Test Cases___
    no cards
    0
    Jack of Clubs
    
    10
    Jack of Clubs
    8 of Spades
    
    18
    Jack of Clubs
    8 of Spades
    10 of Diamonds
    
    28
    ___EXTRA CREDIT___
    
    **Pickle Test**
    Jack of Clubs
    8 of Spades
    10 of Diamonds
    
    Jack of Clubs
    8 of Spades
    10 of Diamonds
    
    Contents of h3 and h4 match!
    
    Process finished with exit code 0
'''