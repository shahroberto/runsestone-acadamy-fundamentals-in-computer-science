def toStr(n,base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base,base) + convertString[n%base]

def backStr(oldstring):
    if len(oldstring) == 0:
        return oldstring
    else:
        return backStr(oldstring[1:]) + oldstring[0]

print(toStr(1453,2))
print(backStr(str(raw_input("Please enter the string to be reversed:\n>"))))
