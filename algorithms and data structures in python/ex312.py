"""Implement a Queue in Python by defining a new type."""


class Queue:
    """Create a queue data type."""

    def __init__(self):
        """Create the empty structure upon intsantiation."""
        self.items = []

    def isEmpty(self):
        """Check if the queue is empty."""
        return self.items == []

    def enqueue(self, item):
        """Define the enqueue attribute."""
        self.items.insert(0, item)

    def dequeue(self):
        """Define the dequeue attribute."""
        return self.items.pop()

    def size(self):
        """Check the size of the items."""
        return len(self.items)


def main():
    """Make main body of script."""
    q = Queue()

    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(True)
    print(q.size())


if __name__ == "__main__":
    """Run on main."""
    main()
