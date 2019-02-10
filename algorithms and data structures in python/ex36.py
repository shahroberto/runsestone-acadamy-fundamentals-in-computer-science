"""How to use a stack.

Implements a stack to determine whether the string of parentheses are
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
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False


def main():
    """Make main body of script."""
    print(parChecker('((()))'))
    print(parChecker('(()'))


if __name__ == "__main__":
    """Run on main."""
    main()
