"""The binary search algorithm without using the slice operator."""


def binarySearchR(alist, item, start, end):
    """Binary search using recursion."""
    if start > end:
        return False
    else:
        midpoint = (end + start) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearchR(alist, item, start, midpoint - 1)
            else:
                return binarySearchR(alist, item, midpoint + 1, end)


def main():
    """Execute main code."""
    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]

    print(binarySearchR(testlist, 3, 0, len(testlist) - 1))
    print(binarySearchR(testlist, 13, 0, len(testlist) - 1))


if __name__ == "__main__":
    main()
