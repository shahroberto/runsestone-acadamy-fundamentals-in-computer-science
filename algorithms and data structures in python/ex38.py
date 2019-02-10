"""Decimal to anyBase converter using stacks.

Implement the Divide by divisor algorithm.
"""

from pythonds import Stack


def baseConverter(decNumber, base):
    """Choose the base."""
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString += digits[remstack.pop()]

    return newString


def main():
    """Make main body of script."""
    print(baseConverter(int(input("Enter a base 10 integer:\n>")),
                        int(input("And the base you wish to convert to:\n>"))))


if __name__ == "__main__":
    """Run on main."""
    main()
