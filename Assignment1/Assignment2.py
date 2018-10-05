"""
    Vanessa Ulloa
    CS21A
    04 October 2018
"""

#
letter = 'Dear %s \nI would ike you to vote for %s\nbecause I think %s is best for\nthis country. \nSincerely, %s\n'
firstLetter = ('Hildegard', 'Hillary Clinton', 'Hillary Clinton', 'Brunhilda')
secondLetter = ('Cheech', 'Donald Trump', 'Donald Trump', 'Chong')
thirdLetter = ('Moe', 'Bernie Sanders', 'Bernie Sanders', 'Jack')

letterInputs = list(firstLetter)
letterInputs.append(list(secondLetter))
letterInputs.append(thirdLetter)

print(letter % firstLetter)
print(letterInputs[0])
"""print(letter % letterInputs[1])
print(letter % letterInputs[2])"""

#   OUTPUT
"""

"""