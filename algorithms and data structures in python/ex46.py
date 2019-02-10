"""Stack frames, implementing recursion without using recursion."""

from pythonds.basic.stack import Stack

rStack = Stack()


def toStr(n, base):
    """Convert a number to a string."""
    convertString = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            rStack.push(convertString[n])
        else:
            rStack.push(convertString[n % base])
        n = n // base
    res = ""
    while not rStack.isEmpty():
        res += str(rStack.pop())
    return res


def main():
    """Make main body of script."""
    print(toStr(1453, 16))


if __name__ == "__main__":
    """Run on main."""
    main()
