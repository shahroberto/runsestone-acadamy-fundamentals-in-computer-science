def removeVowels(s):
    vowels = "aeiouAEIOU"
    sWithoutVowels =  ""
    for eachChar in s:
        if eachChar not in vowels:
            sWithoutVowels += eachChar
    return sWithoutVowels
print(removeVowels("compsci"))
print(removeVowels("aAbEefIijOopUus"))
