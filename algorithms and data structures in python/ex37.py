"""How to use a stack part 2.

Implements a stack to determine whether the string of symbols are
balanced or not.
"""

from pythonds.basic.stack import Stack


def parChecker(symbolString):
    """Check if parantheses are balanced."""
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False


def matches(open, close):
    """Check to see if symbols match."""
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)


def main():
    """Make main body of script."""
    print(parChecker('{{([][])}()}'))
    print(parChecker('[{()]'))


if __name__ == "__main__":
    """Run on main."""
    main()
