"""
    Vanessa Ulloa
    CS21A
    04 October 2018
"""

# Write a program that takes 3 different tuples with entries for adressee, candidate, sender
# print 3 form letters using the tuple values.

letter = 'Dear %s \nI would ike you to vote for %s\nbecause I think %s is best for\nthis country. \nSincerely, %s\n'
firstLetter = 'Hildegard', 'Hillary Clinton', 'Brunhilda'
secondLetter = 'Cheech', 'Donald Trump', 'Chong'
thirdLetter = 'Moe', 'Bernie Sanders', 'Jack'

letterInputs = []
letterInputs.append(list(firstLetter))
letterInputs.append(list(secondLetter))
letterInputs.append(list(thirdLetter))

print(letter % (letterInputs[0][0], letterInputs[0][1], letterInputs[0][1], letterInputs[0][2]))
print(letter % (letterInputs[1][0], letterInputs[1][1], letterInputs[1][1], letterInputs[1][2]))
print(letter % (letterInputs[2][0], letterInputs[2][1], letterInputs[2][1], letterInputs[2][2]))

#   OUTPUT
"""
Dear Hildegard 
I would ike you to vote for Hillary Clinton
because I think Hillary Clinton is best for
this country. 
Sincerely, Brunhilda

Dear Cheech 
I would ike you to vote for Donald Trump
because I think Donald Trump is best for
this country. 
Sincerely, Chong

Dear Moe 
I would ike you to vote for Bernie Sanders
because I think Bernie Sanders is best for
this country. 
Sincerely, Jack


Process finished with exit code 0
"""