julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
print(julia[2])
print(julia[2:6])

print(len(julia))

for field in julia:
    print(field)

julia = julia[:3] + ("Eat Pray Love", 2010) + julia[5:]
print(julia)

tup = (5,)
print(type(tup))

x = (5)
print(type(x))
# ------------------------------------------------------------------------------
# Tuples can assign varibles on the right hand side to the left hand side as long as they are the same length.
# (name, surname, birth_year, movie, movie_year, profession, birth_place) = julia

# temp = a
# a = b
# b = temp

# through tuple assignments
# (a, b) = (b, a)
# -------------------------------------------------------------------------------
def circleInfo(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2*3.14159*r
    a = 3.14159*r*r
    return (c, a)

print(circleInfo(10))
