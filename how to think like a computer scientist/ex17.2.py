import fractions

myfraction = fractions.Fraction(12, 16)

print(myfraction)
myfraction.simplify()
print(myfraction)

myfraction = fractions.Fraction(3, 4)
yourfraction = fractions.Fraction(3, 4)
print(myfraction is yourfraction)

ourfraction = myfraction
print(myfraction is ourfraction)

def sameFraction(f1, f2):
    return (f1.getNum() == f2.getNum()) and (f1.getDen() == f2.getDen())

myfraction = fractions.Fraction(3, 4)
yourfraction = fractions.Fraction(3, 4)
print(myfraction is yourfraction)
print(sameFraction(myfraction, yourfraction))
print(myfraction == yourfraction)
