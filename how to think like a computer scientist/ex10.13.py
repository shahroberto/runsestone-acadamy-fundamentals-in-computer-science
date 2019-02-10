origlist = [45, 76, 34, 55]
print(origlist * 3)

newlist = [origlist]*3

print(newlist)

origlist[1] = 99

print(newlist)
