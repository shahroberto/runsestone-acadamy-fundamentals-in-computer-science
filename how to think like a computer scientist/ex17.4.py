import fractions

f1 = fractions.Fraction(1, 2)
f2 = fractions.Fraction(1, 4)

f3 = f1 + f2    # calls the __add__ method of f1
print(f3 )
