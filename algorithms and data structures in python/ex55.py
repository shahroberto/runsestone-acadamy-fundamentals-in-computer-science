"""Hashing.  Create a map using hash tables."""


class HashTable:
    """Create a hash table."""

    def __init__(self):
        """Initialize the object."""
        self.size = 11  # In this case it is arbitrary but it should prime
        # Create 2 parallel lists
        self.slots = [None] * 11  # Keys
        self.data = [None] * 11  # Data

    # def hashfunction(astring, tablesize):
    #     """Create hash function folding method for chars and a weight."""
    #     sum = 0
    #     for pos in range(len(astring)):
    #         sum += (ord(astring[pos]) * pos)
    #
    #     return (sum % tablesize)

    def put(self, key, data):
        """Put function using open adressing method."""
        if self.len() / len(self.slots) >= 0.80:
            self.slots += [None] * (self.size // 10)
            self.data += [None] * (self.size // 10)

        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # replace the data
            else:
                successor = 1
                nextslot = self.rehash(hashvalue, len(self.slots), successor)
                while self.slots[nextslot] is not None and \
                        self.slots[nextslot] != key:
                    successor += 1
                    nextslot = self.rehash(nextslot, len(self.slots),
                                           successor)

                if self.slots[nextslot] is None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data  # replace data

    def hashfunction(self, key, size):
        """Define the hashfunction."""
        return key % size

    def find(self, key):
        """Find the data."""
        stop = False
        found = False
        startslot = self.hashfunction(key, len(self.slots))
        position = startslot
        successor = 1
        while not found and not stop:
            if self.slots[position] == key:
                found = True
            else:
                position = self.rehash(startslot, len(self.slots), successor)
                successor += 1
                if position == startslot:
                    stop = True
        return (position, stop)

    def rehash(self, oldhash, size, i):
        """Rehash using +1 linear probing."""
        return (oldhash + i) % size

    def get(self, key):
        """Get the data from an associated key."""
        position, flag = self.find(key)
        if flag:
            return "{} is not in the map.".format(key)
        else:
            return self.data[position]

    def __getitem__(self, key):
        """Get item."""
        return self.get(key)

    def __setitem__(self, key, data):
        """Set item."""
        self.put(key, data)

    def __len__(self):
        """Return the length of the Map."""
        count = 0
        for i in self.slots:
            if i is not None:
                count += 1
        return count

    def len(self):
        """Help __len__."""
        return self.__len__()

    def delete(self, key):
        """Find and delete a desired item."""
        position, flag = self.find(key)
        if flag:
            print("{} is not in the map.".format(key))
        else:
            self.slots[position] = None
            self.data[position] = None
            position += 1
            while self.slots[position] is not None:
                newKey = self.slots[position]
                newData = self.data[position]
                self.slots[position] = None
                self.data[position] = None
                self.put(newKey, newData)
                position += 1


def main():
    """Execute main code."""
    H = HashTable()
    H[54] = "cat"
    H[26] = "dog"
    H[93] = "lion"
    H[17] = "tiger"
    H[77] = "bird"
    H[31] = "cow"
    H[44] = "goat"
    H[55] = "pig"
    H[20] = "chicken"
    print(H.slots)
    print(H.data)

    print(H[20])
    print(H[17])
    H[20] = 'duck'
    print(H[20])
    print(H[99])
    print(H.len())
    H.delete(20)
    print(H.len())
    print(H.slots)
    print(H.data)


if __name__ == "__main__":
    main()
