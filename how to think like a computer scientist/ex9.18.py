def find4(astring, achar, start=0, end=None):
    """
    Find and return the index of achar in astring.
    Return -1 if achar does not occur in astring.
    """
    ix = start
    found = False
    while ix < len(astring) and not found:
        if astring[ix] == achar:
            found = True
        else:
            ix += 1
    if found:
        return ix
    else:
        return -1

ss = "Python strings have some interesting methods."

print(find4(ss,'s'))
print(find4(ss,'s',7))
print(find4(ss,'s',8))
print(find4(ss,'s',8,13)) # in this program 2 is an optional parameter
# if nothing is inserted then it will default to start = 0.
print(find4(ss,'.'))
