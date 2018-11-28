"""
    Vanessa Ulloa
    CS21A
    27 November 2018
    Assignment 9
"""

from hand import Hand

# Test Class

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




# Output
