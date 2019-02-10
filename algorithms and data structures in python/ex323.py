"""Implement an ordered list (linked list) in python."""


class Node:
    """Construct the node of the linked list."""

    def __init__(self, initdata, position=0):
        """Initialize the node."""
        self.data = initdata
        self.next = None
        self.position = position

    def getData(self):
        """Access node data."""
        return self.data

    def getNext(self):
        """Point to the next node."""
        return self.next

    def setData(self, newdata):
        """Change the data in the node."""
        self.data = newdata

    def setNext(self, newnext):
        """Change the next node pointed to."""
        self.next = newnext


class OrderedList:
    """Implement an ordered list."""

    def __init__(self):
        """Initialize the list."""
        self.head = None

    def isEmpty(self):
        """Check to see if the list is empty."""
        return self.head is None

    def size(self):
        """Return the size of the list."""
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def remove(self, item):
        """Search and remove item from list."""
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        self.index_correct(self.head)

    def index_correct(self, item):
        """Correct the index of each node."""
        position = item.position
        value = item
        while value is not None:
            value.position = position
            position += 1
            value = value.next

    def search(self, item):
        """Find the item in the list."""
        current = self.head
        found = False
        stop = False
        while current is not None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found

    def add(self, item):
        """Add a value to the list."""
        current = self.head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        temp = Node(item)
        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
        self.index_correct(self.head)

    def __str__(self):
        """Print the list when needed."""
        theList = []
        current = self.head
        while current is not None:
            theList.append((current.getData(), current.position))
            current = current.getNext()
        return (str(theList))


def main():
    """Make main body of script."""
    mylist = OrderedList()
    mylist.add(17)
    mylist.add(26)
    mylist.add(54)
    mylist.add(77)
    mylist.add(93)
    print(mylist)
    mylist.add(31)
    print(mylist)


if __name__ == "__main__":
    """Run on main."""
    main()
