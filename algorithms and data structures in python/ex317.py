"""Implenting a deque in python."""


class Deque:
    """Implement a deque in python."""

    def __init__(self):
        """Initialize the class."""
        self.items = []

    def isEmpty(self):
        """Check to see if deque is empty."""
        return self.items == []

    def addFront(self, item):
        """Add and item to the front."""
        self.items.append(item)

    def addRear(self, item):
        """Add an item to the rear."""
        self.items.insert(0, item)

    def removeFront(self):
        """Remove the front item."""
        return self.items.pop()

    def removeRear(self):
        """Remove the rear item."""
        return self.item.pop(0)

    def size(self):
        """Return the size of the deque."""
        return len(self.items)


def main():
    """Make main body of script."""
    pass


if __name__ == "__main__":
    """Run on main."""
    main()
