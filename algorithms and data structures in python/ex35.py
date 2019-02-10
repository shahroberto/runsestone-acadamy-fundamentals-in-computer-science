"""Implent a stack type using Python.

This module is the intro to creating and using stacks in Python.  This is
performed by creating a stack type class.  Use it to reverse a string.
"""


class Stack:
    """Create stack."""

    def __init__(self):
        """Inilitize an empty stack."""
        self.items = []

    def isEmpty(self):
        """Check if Stack is empty."""
        return self.items == []

    def push(self, item):
        """Push new item to stack."""
        self.items.append(item)

    def pop(self):
        """Pop top item from stack."""
        return self.items.pop()

    def peek(self):
        """Peek at top stack item."""
        return self.items[len(self.items) - 1]

    def size(self):
        """Return the length of the stack."""
        return len(self.items)

    def join(self):
        """Join all elemts of a stack into a string."""
        return ''.join(self.items)

    def __str__(self):
        """Return the str of the list when printed."""
        return str(self.items)


def revstring(l):
    """Reverse a string."""
    m = Stack()
    for i in range(len(l) - 1, -1, -1):
        m.push(l[i])
    return m


def main():
    """Make main body of script."""
    myStr = 'Robert Shaheen'
    print(revstring(myStr).join())


if __name__ == "__main__":
    """Run on main."""
    main()
