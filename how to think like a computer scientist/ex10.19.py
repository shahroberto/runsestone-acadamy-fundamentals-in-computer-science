def doubleStuff(aList):
    """ Return a new list which contains doubles of each element in aList. """
    newList = []
    for value in aList:
        newElem = 2 * value
        newList.append(newElem)
    return newList

things = [2, 5, 9]
print(things)
things = doubleStuff(things)
print(things)
