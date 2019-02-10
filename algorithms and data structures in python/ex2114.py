"""Find the kth smallest number in a list of n numbers."""


def merge(a, b):
    """Merge two arrays."""
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c


def sort(l):
    """Sort the list in an n*logn time using Mergesort."""
    if len(l) == 0 or len(l) == 1:
        return l
    else:
        middle = len(l) // 2
        a = sort(l[:middle])
        b = sort(l[middle:])
        return merge(a, b)


def main():
    """Execute main body."""
    array = [2, 4, 5, 7, 4, 2]
    copy = array[:]
    k = int(input("Find kth smallest number:\n>"))
    final = sort(copy)
    print(final)
    print("{} smallest number in {} is: {}".format(k, array, final[k - 1]))


if __name__ == "__main__":
    """Execute main() on access."""
    main()

# To improve the time complexity to linear I would assume that one
# should employ a hash table (O(n)) and then select the kth contender (O(1)).
