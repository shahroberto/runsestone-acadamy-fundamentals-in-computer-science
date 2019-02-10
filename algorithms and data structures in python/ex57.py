"""The Bubble Sort.

The first function is a standard bubble sort.  The second is modified to
stop early if it discovers that the list is sorted (ie no exchanges during a
pass).
"""


def bubbleSort(alist):
    """Sort an array using the bubble sort."""
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                # This chunk is traditional however Python supports
                # simeoultaneous assignment i.e. a,b = b,a
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp


def shortBubbleSort(alist):
    """Sort the array using a bubble sort but stop when it is sorted."""
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
        passnum -= 1


def main():
    """Execute main body of code."""
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubbleSort(alist)
    print(alist)

    alist = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
    shortBubbleSort(alist)
    print(alist)


if __name__ == "__main__":
    main()
