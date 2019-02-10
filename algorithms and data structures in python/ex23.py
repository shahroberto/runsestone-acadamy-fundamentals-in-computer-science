"""Write 2 functions that determine the minimum number in a list."""
__author__ = "Robert Shaheen"
import random as r
import timeit


def minSquare(l):
    """Find min val in array in n^2 time."""
    win = l[0]
    for n in l:
        issmallest = True
        for j in l:
            if n > j:
                issmallest = False
        if issmallest:
            win = n
    return win


def minLinear(l):
    """Find min val in array in n time."""
    win = l[0]
    for n in l:
        if n < win:
            win = n
    return win


def main():
    """Execute Main()."""
    array = r.sample(range(100), 10)
    n2_array = array[:]
    n_array = array[:]
    print(array)
    time1 = timeit.timeit()
    print(minSquare(n2_array))
    time2 = timeit.timeit()
    print(time2 - time1)
    print(minLinear(n_array))
    time3 = timeit.timeit()
    print(time3 - time2)


if __name__ == "__main__":
    main()
