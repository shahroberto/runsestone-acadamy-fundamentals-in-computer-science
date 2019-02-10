def newtonSqrt(n):
    """Find the sqrt of a numiber using newtons method."""
    approx = 0.5*n
    better = 0.5*(approx + n/approx)
    while better != approx:
        approx = better
        better = 0.5*(approx + n/approx)
    return approx

print(newtonSqrt(10))
