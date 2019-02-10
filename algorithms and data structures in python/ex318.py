"""Palindrome checker using a deque."""

from pythonds.basic.deque import Deque


def palchecker(aString):
    """Check if the string is a palindrome."""
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual


def main():
    """Make main body of script."""
    print(palchecker("lsdkjfskf"))
    print(palchecker("radar"))


if __name__ == "__main__":
    """Run on main."""
    main()
