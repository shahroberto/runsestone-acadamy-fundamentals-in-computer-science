def countAll(phrase):
    numLetters = {}
    phrase = phrase.lower()
    for char in phrase:
        if char.isalpha():
            flag = True
            for key in numLetters:
                if key == char:
                    flag = False
            if flag:
                numLetters[char] = 1
            else:
                numLetters[char] += 1
    return numLetters
