"""The Shell Sort."""


def shellSort(alist):
    """Sort the list using a shell sort."""
    sublistcount = len(alist) // 2  # define number of sublists
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)

        print("After increments of size", sublistcount, "The list is", alist)
        sublistcount = sublistcount // 2


def gapInsertionSort(alist, start, gap):
    """Sorting the gap insertion."""
    for i in range(start + gap, len(alist), gap):
        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position -= gap

        alist[position] = currentvalue


def main():
    """Execute main code."""
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    shellSort(alist)
    print(alist)


if __name__ == "__main__":
    main()
