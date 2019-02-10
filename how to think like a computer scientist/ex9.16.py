def count(text, aChar):
    lettercount = 0
    for c in text:
        if c == aChar:
            lettercount += 1
    return lettercount

print(count("banana","a"))
