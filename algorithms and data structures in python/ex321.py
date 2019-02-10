"""Implement an unordered list (linked list) in python."""


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


class UnorderedList:
    """Create the class that links the nodes together."""

    def __init__(self):
        """Initialize the class."""
        self.head = None
        self.tail = None

    def isEmpty(self):
        """Check to see if the list is empty."""
        return self.head is None

    def add(self, item):
        """Add a node to the list."""
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        current = self.head
        self.index_correct(current)
        current = self.head
        while current.position != self.size() - 1:
            current = current.next
        if temp.getNext() is None:
            self.tail = temp

    def index_correct(self, item):
        """Correct the index of each node."""
        position = item.position
        value = item
        while value is not None:
            value.position = position
            position += 1
            value = value.next

    def size(self):
        """Return the size of the list."""
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        """See if an element is in the list."""
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

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

    def append(self, item):
        """Append an item to the end of the list."""
        current = self.tail
        if current:
            current.setNext(Node(item))
            lastNode = current.getNext()
        else:
            self.head = Node(item)
        self.tail = current
        lastNode.position = self.size() - 1

    def index(self, item):
        """Retrieve the index value of the node."""
        current = self.head
        while current is not None:
            if current.data == item:
                return current.position
            else:
                current = current.getNext()
        print("Item not present in list.")

    def insert(self, item, position):
        """Insert a node at a given position."""
        if position == 0:
            self.add(item)
        elif position > self.size():
            print("Position index out of range.")
        elif position == self.size():
            self.append(item)
        else:
            temp = Node(item, position)
            current = self.head
            previous = None
            while current.position != position:
                previous = current
                current = current.next
            previous.next = temp
            temp.next = current
            current = self.head
            self.index_correct(current)

    def pop(self, position):
        """Pop an item from the list."""
        current = self.head
        while current is not None:
            if current.position == position:
                self.remove(current.data)
                return current.data
            else:
                current = current.next
        if current is None:
            print("Index is out of bounds.")

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
    mylist = UnorderedList()
    mylist.add(31)
    mylist.add(77)
    mylist.add(26)
    mylist.add(54)
    mylist.append(666)
    mylist.insert(777, 3)
    mylist.remove(17)
    mylist.add(12)
    mylist.add(34)
    mylist.add('Robert')
    mylist.add(69)
    mylist.add(45)
    mylist.add(52)
    print(mylist)
    print(mylist.pop(4))
    print(mylist)


if __name__ == "__main__":
    """Run on main."""
    main()
