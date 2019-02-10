def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm % oldn
    return n

print(gcd(12, 16))

class Fraction:

    def __init__(self, top, bottom):
        self.num = top      # numerator
        self.den = bottom   # denominator

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def simplify(self):
        common = gcd(self.num, self.den)
        self.num = self.num // common
        self.den = self.den // common

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    def __add__(self, otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den*otherfraction.den

        common = gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)

def main():
    myfraction = Fraction(3, 4)
    print(myfraction)

    print(myfraction.getNum())
    print(myfraction.getDen())

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   main()
