def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

def rev(l):
    if not l: return []
    else:
        return rev(l[1:]) + [l[0]]

things = [1,2,3,4,5]
print(rev(things))
