"""
    Vanessa Ulloa
    CS21A
    20 October 2018
    Assignment 3
"""

# this program contains several dictionaries that will be combined into a new dictionary with unique keys

roommate1Shopping = {'fruit': 'apples', 'meat': 'chicken', 'vegetables': 'potatoes', 'drinks': ['beer','wine'], 'dessert': 'ice cream'}
roommate2Shopping = {'fruit': 'lemons', 'meat': 'hamburger', 'drinks': ['apple juice', 'orange juice', 'vodka']}
roommate3Shopping = {'fruit': ['oranges', 'bananas'], 'vegetables': ['lettuce', 'carrots'], 'drinks': 'milk'}


# resulting dictionary
mergedDict = roommate1Shopping.copy()

# process the 2nd dictionary
for key, value in roommate2Shopping.items():
    if key not in mergedDict:
        mergedDict[key] = value
    else:
        tempList = []
        if isinstance(value, list):
            tempList.extend(value)
        else:
            tempList.append(value)
        oldValue = mergedDict[key]
        if isinstance(oldValue, list):
            tempList.extend(oldValue)
        else:
            tempList.append(oldValue)
        mergedDict[key] = tempList

# process the 3rd dictionary
for key, value in roommate3Shopping.items():
    if key not in mergedDict:
        mergedDict[key] = value
    else:
        tempList = []
        if isinstance(value, list):
            tempList.extend(value)
        else:
            tempList.append(value)
        oldValue = mergedDict[key]
        if isinstance(oldValue, list):
            tempList.extend(oldValue)
        else:
            tempList.append(oldValue)
        mergedDict[key] = tempList

print('original dictionaries:')
print(roommate1Shopping)
print(roommate2Shopping)
print(roommate3Shopping)

print('resulting dictionary:')
print(mergedDict)

#   OUTPUT
"""
original dictionaries:
{'fruit': 'apples', 'meat': 'chicken', 'vegetables': 'potatoes', 'drinks': ['beer', 'wine'], 'dessert': 'ice cream'}
{'fruit': 'lemons', 'meat': 'hamburger', 'drinks': ['apple juice', 'orange juice', 'vodka']}
{'fruit': ['oranges', 'bananas'], 'vegetables': ['lettuce', 'carrots'], 'drinks': 'milk'}
resulting dictionary:
{'fruit': ['oranges', 'bananas', 'lemons', 'apples'], 'meat': ['hamburger', 'chicken'], 'vegetables': ['lettuce', 'carrots', 'potatoes'], 'drinks': ['milk', 'apple juice', 'orange juice', 'vodka', 'beer', 'wine'], 'dessert': 'ice cream'}

Process finished with exit code 0
"""