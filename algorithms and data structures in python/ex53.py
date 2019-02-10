"""Sequential search examples."""


def sequentialSearch(alist, item):
    """Sequentially search a linear structure for a value."""
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1

    return found


def orderedSequentialSearch(alist, item):
    """Sequentially search an ordered list."""
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos += 1

    return found


def main():
    """Execute main code."""
    # Seqiential search.
    testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    print(sequentialSearch(testlist, 3))
    print(sequentialSearch(testlist, 13))

    # Ordered sequential search.
    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(orderedSequentialSearch(testlist, 3))
    print(orderedSequentialSearch(testlist, 13))


if __name__ == "__main__":
    main()
