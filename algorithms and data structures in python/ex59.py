"""The Insertion Sort.

Bases its integrity from a shift instead of exchange.  A shift requires
about 1/3 of the processing power therefore insertion sort will show very
good performance.
"""


def insertionSort(alist):
    """Use an insertion sort to sort an array."""
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position -= 1

        alist[position] = currentvalue


def main():
    """Execute main code of the function."""
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insertionSort(alist)
    print(alist)


if __name__ == "__main__":
    main()
